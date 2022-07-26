from django.views import View
from django.shortcuts import render,redirect
from crm1.forms.forms import OrderForm
from crm1.models import Order

class UpdateOrderViews(View):
    template_name = 'crm1/order_form.html'
    title = ("Update order page")
    def post(request,pk):
        order = Order.objects.get(id=pk)
        form = OrderForm(instance=order)
        if request.method == 'POST':
            form = OrderForm(request.POST,instance=order)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form':form}

        return render(request,'crm1/order_form.html',context)