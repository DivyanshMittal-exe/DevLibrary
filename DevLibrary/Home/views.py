from django.shortcuts import render,redirect
from book.models import Book

# Create your views here.
def home_view(request,*args,**kwargs):
    books = Book.objects.all()
    if request.user.groups.filter(name="Librarian"):
        return render(request,"Home/home-librarian.html",{"books":books})
    else:
        return render(request,"Home/home.html",{"books":books})

def login_view(request,*args,**kwargs):
    return render(request,"Login/Login.html")

def sign_view(request,*args,**kwargs):
    return render(request,"SignUp/SignUp.html")