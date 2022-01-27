from datetime import datetime
from turtle import title
from django.db import models

class Todos(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000,blank=True)
    finished=models.BooleanField(default=True)
    date=models.DateTimeField(default=datetime.now, blank=True)

    

    def __str__(self):
        return self.title

   

# Create your models here.
