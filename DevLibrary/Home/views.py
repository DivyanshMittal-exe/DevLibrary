from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"Home/home.html")

def login_view(request,*args,**kwargs):
    return render(request,"Login/Login.html")

def sign_view(request,*args,**kwargs):
    return render(request,"SignUp/SignUp.html")