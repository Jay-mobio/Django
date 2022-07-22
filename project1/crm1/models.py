from operator import mod
from pyexpat import model
from sre_parse import CATEGORIES
from statistics import mode
from bs4 import Tag
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null = True)
    phone = models.CharField(max_length=200,null = True)
    email = models.CharField(max_length=200,null = True)
    profile_pic = models.ImageField(null=True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null = True)    
    def __str__(self):
        return self.name

class Products(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name = models.CharField(max_length=200, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length=200, null = True, choices=CATEGORY)
    discreption = models.CharField(max_length=200, null = True, blank=True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('delivered','delivered'),
    )
    customer = models.ForeignKey(Customer , null=True , on_delete=models.SET_NULL)
    products = models.ForeignKey(Products , null=True , on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    status = models.CharField(max_length=200,null = True,choices=STATUS)

    def __str__(self):
        return self.products.name

class UserRegister(models.Model):
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField(max_length=200, null = True)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)

class FeedBack(models.Model):
	username = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	product = models.CharField(max_length=200)
	feedback = models.TextField()