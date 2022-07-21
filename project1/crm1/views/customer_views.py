from django.views import View


from crm1.models import Customer
from django.shortcuts import render

class CustomerViews(View):
    template_name = 'crm1/customer.html'
    title = ("Customer Page")
    def get(request,pk):
        customer = Customer.objects.get(id=pk)
        orders = customer.order_set.all()
        order_count = orders.count()
        context = {'customer':customer,'orders':orders,'order_count':order_count}
        return render(request,'crm1/customer.html',context)