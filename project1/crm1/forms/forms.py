from dataclasses import field
import email
from tkinter.tix import Form
import django
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.views.generic.edit import FormView
django



from ..models import *


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserRegister(UserCreationForm):
	class Meta:
		model = User
		fields = ["username","password1","email","password2"]

class FeedBackForm(ModelForm):
	username = forms.CharField(max_length=200)
	email = forms.EmailField(max_length=200)
	product = forms.CharField(max_length=200)
	feedback = forms.Textarea()

	class Meta:
		model = FeedBack
		fields = ['username','email','product','feedback']

	# def clean(self):
	# 	cleaned_data = super(FeedBackForm,self).clean()
	# 	name = cleaned_data.get('username')
	# 	email = cleaned_data.get('email')
	# 	product = cleaned_data.get('product')
	# 	feedback = cleaned_data.get('feedback')
