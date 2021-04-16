from django.shortcuts import render

from.models import Book
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
def book_view(request,*args,**kwargs):
    obj=Book.objects.get(id=1)

    content={
        "title":obj.Title,
        "auth":obj.Author,
        "pub":obj.Publisher,
        "gen":obj.Genre,
        "isbn":obj.ISBN,
        "loc":obj.Location,
        "comm":obj.Comments
    }

    return render(request,"Books/book.html",content)