from django.views import View
from django.forms import inlineformset_factory
from crm1.models import Customer,Order
from django.shortcuts import render,redirect



class CreateOrderViews(View):
    template_name = 'crm1/order_form.html'
    title = ("Create order page")
    def post(request,pk):
        OrderFormSet = inlineformset_factory(Customer,Order,fields=('products','status',),extra=10)
        customer = Customer.objects.get(id=pk)
        # formset = OrderFormSet(request.POST,instance=customer)
        formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
        # form = OrderForm(initial={'customer':customer})
        if request.method == 'POST':
            # form = OrderForm(request.POST)
            formset = OrderFormSet(request.POST, instance=customer)
            if formset.is_valid():
                formset.save()
                return redirect('/')
        context = {'formset':formset}
        return render(request,'crm1/order_form.html',context)