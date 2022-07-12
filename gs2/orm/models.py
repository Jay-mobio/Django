from operator import mod
from django.db import models
from django.forms import CharField, EmailField, IntegerField


# Create your models here.
class Student(models.Model):

    stuid=  models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)