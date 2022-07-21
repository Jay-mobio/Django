from crm1.models import Products
from django.shortcuts import render
from django.views import View

class ProductViews(View):
    title = ("Product page")
    template_name = 'crm1/products.html'
    def get(request):
        products = Products.objects.all()
        return render(request,'crm1/products.html',{'products':products})