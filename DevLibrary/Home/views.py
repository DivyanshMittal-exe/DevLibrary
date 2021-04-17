from django.shortcuts import render
from book.models import Book

# Create your views here.
def home_view(request,*args,**kwargs):
    
    books = Book.objects.all()
    
    return render(request,"Home/home.html",{"books":books})

def login_view(request,*args,**kwargs):
    return render(request,"Login/Login.html")

def sign_view(request,*args,**kwargs):
    return render(request,"SignUp/SignUp.html")