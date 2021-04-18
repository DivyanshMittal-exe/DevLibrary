from django.shortcuts import render,redirect
from django.contrib import messages
import datetime
from django.utils import timezone
from .models import Book,Issue
from .forms import BookForm


# Create your views here.


def book_from_view(request,*args,**kwargs):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()

    content={
        "form": form
    }

    return render(request,"Books/NewBook.html",content)



# Create your views here.
def book_view(request,id,*args,**kwargs):
    obj=Book.objects.get(id=id)
    ID = id
    if request.method =='POST':
        title = obj.Title
        bookid= obj.id 
        user = request.user 
        iss = Issue(Title=title,BookID=bookid,User=user,DoI=datetime.date.today(),DoD = datetime.timedelta(7))
        iss.save()
        messages.info(request, 'Book issue request placed')
        content={
            "title":obj.Title,
            "auth":obj.Author,
            "pub":obj.Publisher,
            "gen":obj.Genre,
            "isbn":obj.ISBN,
            "loc":obj.Location,
            "comm":obj.Comments,
            "avlbl":obj.Available,
            "id":obj.id
        }
        
        return render(request,"Books/book.html",content)
    else:
        content={
            "title":obj.Title,
            "auth":obj.Author,
            "pub":obj.Publisher,
            "gen":obj.Genre,
            "isbn":obj.ISBN,
            "loc":obj.Location,
            "comm":obj.Comments,
            "avlbl":obj.Available,
            "id":obj.id
        }
        return render(request,"Books/book.html",content)