from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'crud_app/home.html')

def form(request):
    return render(request,'crud_app/form.html')


