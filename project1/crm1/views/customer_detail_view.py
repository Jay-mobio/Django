from django.shortcuts import render
from crm1.models import Customer
from django.views.generic.detail import DetailView

class CustomerDetailViews(DetailView):
    model = Customer