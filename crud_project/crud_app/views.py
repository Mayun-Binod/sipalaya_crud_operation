from django.shortcuts import render, redirect
from .models import Student_Detail
from django.contrib import messages

def home(request):
    stud = Student_Detail.objects.all() 
    return render(request, 'crud_app/home.html', {"stud": stud})

def about(request):
    return render (request,'crud_app/about.html')

def contact(request):
    return render (request,'crud_app/contact.html')


def form(request):
    try:
         if request.method == "POST":
          fm = request.POST
          fn = fm.get('name') # or fn=fm['name']
          age = fm.get('age')
          em = fm.get('email')
          mssg = fm.get('message')

         if int(age)<1 or int(age)>100:
            messages.error(request,"your age must be between 1-100")
            return redirect('form')  

         if fn and age and em and mssg:  
            store = Student_Detail(full_name=fn, age=age, email=em, message=mssg)
            store.full_clean()
            store.save()
            messages.success(request,f"hi {fn} successfully submitted!!!")
            return redirect('form')
    except Exception as e:
        messages.success(request,f"error:{str(e)}")     
     
    return render(request, 'crud_app/form.html')

