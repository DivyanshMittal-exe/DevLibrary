from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    Title = models.CharField(max_length = 120,null = False)
    Author = models.CharField(max_length = 120)
    Publisher = models.CharField(max_length = 120)
    Genre = models.CharField(max_length = 120)
    ISBN = models.CharField(max_length = 13,null = False) #as int was small, take as char
    Location = models.TextField()
    Available = models.BooleanField(default=True)
    Comments = models.TextField(null=True)

class Issue(models.Model):
    Book_state = [
        ('Requested', 'Requested'),
        ('Issued', 'Issued'),
        ('Returned', 'Returned'),
        ('NA', 'NA')
    ]
    Title = models.CharField(max_length = 120,null = False)
    BookID = models.IntegerField(null = False)
    User = models.CharField(max_length=50)
    DoI=models.DateField(auto_now_add=False)
    DoD=models.DateField(auto_now_add=False)
    State = models.CharField(
        max_length=9,
        choices = Book_state,
        default = 'Requested',
    )
    Comments = models.TextField(null=True)