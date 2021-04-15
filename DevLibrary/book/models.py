from django.db import models


# Create your models here.
class Book(models.Model):
    Title = models.CharField(max_length = 120,null = False)
    Author = models.CharField(max_length = 120)
    Publisher = models.CharField(max_length = 120)
    Genre = models.CharField(max_length = 120)
    ISBN = models.CharField(max_length = 13,null = False) #as int was small, take as char
    Location = models.TextField()
    Available = models.BooleanField(default=True)
