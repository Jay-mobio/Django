from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from crm1.models import *

class home(TemplateView):
        title = ("Display home page")
        template_name = 'crm1/login.html'
        # orders = Order.objects.all()
        # customer = Customer.objects.all()
        # total_customers = customer.count()
        # total_orders = orders.count()  
        # delivered = orders.filter(status='delivered').count() 
        # pending = orders.filter(status='pending').count()
        # context = {'orders':orders,'customer':customer,'total_customers':total_customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}
        # return render (request,'crm1/dashboard.html',context)
