from django.shortcuts import render,redirect
from django.views import View

class UserPageViews(View):
    title = ("User Page")
    template_name = 'crm1/user.html'
    def get(request):
        orders = request.user.customer.order_set.all()
        print('ORDERS:', orders)
        context = {'orders':orders}
        return render(request, 'crm1/user.html',context)