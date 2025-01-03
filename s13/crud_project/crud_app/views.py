from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request):
   searched=request.GET.get('searched')
   if searched:
      data=Student.objects.filter(Q(name__icontains=searched)|Q(age__iexact=searched)|Q(email__icontains=searched))
      data=data.filter(isdelete=False)
   else:
    data=Student.objects.filter(isdelete=False)
   return render(request,'crud_app/home.html',{'data':data})

def form(request):
    try:
        if request.method=='POST':
            name=request.POST['name'] #ram
            age=request.POST['age']
            email=request.POST['email']
            message=request.POST['message']
            
            if int(age)<1 or int(age)>100:
                messages.error(request,'Your age should be between 1 to 100')
                return redirect('form')
            
            user=Student(name=name,age=age,email=email,message=message)
            user.full_clean()
            user.save()
            messages.success(request,f"Hi {name} your form successfully submitted!!!")
            return  redirect('form')
    except Exception as e:
        messages.error(request,f"Error: {str(e)}")
    
    return render(request,'crud_app/form.html')
def about(request):
    return render(request,'crud_app/about.html')
def contact(request):
    return render(request,'crud_app/contact.html')

def delete_data(request,id):#id=7
    data=Student.objects.get(id=id)
    # data.delete() -->hard delete
    data.isdelete=True #soft delete
    data.save()
    return redirect('home')

def edit(request,id):
    data=Student.objects.get(id=id) #
    if request.method=='POST':
        """name=request.POST['name'] #ankit update
        age=request.POST['age']
        email=request.POST['email']
        message=request.POST['message']"""
        data=Student.objects.get(id=id)
        
        data.name=request.POST['name']
        data.age=request.POST['age']
        data.email=request.POST['email']
        data.message=request.POST['message']
        data.save()
        return redirect('home')
    return render(request,'crud_app/edit.html',{'data':data})
    