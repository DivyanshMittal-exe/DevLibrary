from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Q
import datetime
from django.utils import timezone
from .models import Book,Issue,Rates
from .forms import BookForm,IssueForm


# Create your views here.



def req_view(request,*args,**kwargs):
    issues = Issue.objects.all()
    if request.user.groups.filter(name="Librarian"):
        return render(request,"Home/req.html",{"issues":issues,"day":datetime.date.today()})

def reject_book_view(request,id,*args,**kwargs):
    if request.method =='POST':
        isss = Issue.objects.get(id=id)
        isss.State = "Rejected Issue"
        isss.DoD=datetime.datetime.today()
        isss.save()
    return redirect('/req')

def reqext_view(request,id,*args,**kwargs):
    if request.method =='POST':
        isss = Issue.objects.get(id=id)
        isss.State = "Request Extension"
        isss.save()
    return redirect('/user/')

def reqextyes(request,id,*args,**kwargs):
    if request.method =='POST':
        isss = Issue.objects.get(id=id)
        isss.State = "Extended Issue"
        isss.DoD=isss.DoD+datetime.timedelta(days=7)
        isss.save()
    return redirect('/req')

def reqextno(request,id,*args,**kwargs):
    if request.method =='POST':
        isss = Issue.objects.get(id=id)
        isss.State = "Issued/Ext Denied"
        isss.save()
    return redirect('/req')
 
  
def issuereq_view(request,id,*args,**kwargs):
    if request.method =='POST':
        isss = Issue.objects.get(id=id)
        bkid = isss.BookID
        obj=Book.objects.get(id=bkid)
        isss.DoI=datetime.date.today()
        isss.DoD=datetime.date.today()+datetime.timedelta(days=7)
        isss.State = "Issued"
        obj.save()
        isss.save()
    return redirect('/req')
    
def return_book_view(request,id,*args,**kwargs):
    if request.method =='POST':
        isss = Issue.objects.get(id=id)
        bkid = isss.BookID
        obj=Book.objects.get(id=bkid)
        isss.DoD=datetime.date.today()
        isss.State = "Returned"
        obj.Available=True
        obj.save()
        isss.save()
    return redirect('/req')
        
def edit_book_view(request,id,*args,**kwargs):
    obj=Book.objects.get(id=id)
    if request.user.groups.filter(name="Librarian"):
        return render(request,"Books/BookEdit.html",{"id":id,"book":obj})

def edit_save_view(request,id,*args,**kwargs):
    if request.method =='POST':
        obj=Book.objects.get(id=id)
        titlee = request.POST['titl']
        autho = request.POST['auth']
        publee = request.POST['publ']
        genre = request.POST['genr']
        isssbn = request.POST['issbn']
        commenn = request.POST['comme']
        locatt = request.POST['loca']
        mrknaa = request.POST['states']
        obj.Title = titlee
        obj.Author = autho
        obj.Publisher=publee
        obj.Genre =genre
        obj.ISBN=isssbn
        obj.Location =locatt
        obj.Comments = commenn
        
        if mrknaa == "Available":
            obj.Available = True
            obj.Lost= False
        elif mrknaa == "Unavailable":
            obj.Available = False
            obj.Lost= False
        elif mrknaa == "Lost":
            obj.Available = False
            obj.Lost= True 
        
        obj.save()
        
    return redirect('/')

def rate_book(request,id,*args,**kwargs):
    if request.method =='POST':
        usser = request.user 
        bkrate=Book.objects.get(id=id)
        rte = request.POST['star']
        comm = request.POST['comm']
        
        newrate = Rates(
            
            userID = usser.id,
            rates = rte,
            usrrnme= usser.username,
            comment = comm,
            bookID = id
        ) 
        newrate.save()
    return redirect(f'/book/{id}')

def issue_form_view(request,*args,**kwargs):
    form = IssueForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = IssueForm()

    content={
        "form": form
    }

    return render(request,"Books/NewIssue.html",content)       

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
    req=1
    if request.method =='POST':
        title = obj.Title
        bookid= obj.id 
        user = request.user 
        iss = Issue(
            Title=title,
            BookID=bookid,
            User=user,
            DoI=datetime.date.today(),
            DoD=datetime.date.today()+datetime.timedelta(days=7)
            )
        iss.save()
        req = 0
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
            "id":obj.id,
            "req":req
        }
        obj.Available = False
        obj.save()
        return render(request,"Books/book.html",content)
    else:
        bookratings = Rates.objects.filter(bookID=ID)
        fr = float(0)
        l = float(0)
        for rate in bookratings:
            fr = fr + float(rate.rates)
            l=l+1
        if fr!=0:
            fr = float(fr)/l
        else:
            fr = str("No Rating Available")
        
        
        if Rates.objects.filter(bookID=ID,usrrnme = request.user ):
            hasNotRated = False
        else: 
            hasNotRated = True
        
        
        content={
            "title":obj.Title,
            "auth":obj.Author,
            "pub":obj.Publisher,
            "gen":obj.Genre,
            "isbn":obj.ISBN,
            "loc":obj.Location,
            "comm":obj.Comments,
            "avlbl":obj.Available,
            "id":obj.id,
            "req":req,
            "ratigs":bookratings,
            "rt":fr,
            "hasNR":hasNotRated
        }
        return render(request,"Books/book.html",content)