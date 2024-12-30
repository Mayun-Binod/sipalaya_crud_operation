from django.shortcuts import render, redirect
from .models import Student_Detail

def home(request):
    stud = Student_Detail.objects.all() 
    return render(request, 'crud_app/home.html', {"stud": stud})

def form(request):
    if request.method == "POST":
        fm = request.POST
        fn = fm.get('name') # or fn=fm['name']
        age = fm.get('age')
        em = fm.get('email')
        mssg = fm.get('message')

        if fn and age and em and mssg:  
            store = Student_Detail(full_name=fn, age=age, email=em, message=mssg)
            store.save()
            return redirect('home')  
    return render(request, 'crud_app/form.html')
