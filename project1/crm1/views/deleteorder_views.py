from django.views import View
from crm1.models import Order
from django.shortcuts import redirect,render

class DeleteOrdeerViews(View):
    template_name = 'crm1/delete.html'
    title = ("Delete order page")
    def post(request,pk):
        order = Order.objects.get(id=pk)
        if request.method == "POST":
            order.delete()
            return redirect('/')
        context = {'item':order}
        return render(request,'crm1/delete.html',context)