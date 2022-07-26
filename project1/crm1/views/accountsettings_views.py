from django.views import View
from django.shortcuts import render
from ..forms.forms import CustomerForm


class AccountSettingsViews(View):
    title = ("Account settings page")
    template_name = 'crm1/account_settings.html'
    def post(request):
        customer = request.user.customer
        form = CustomerForm(instance=customer)
        if request.method == 'POST':
           form = CustomerForm(request.POST, request.FILES,instance=customer)
           if form.is_valid():
            form.save()    
        context = {'form':form}
        return render(request,'crm1/account_settings.html',context)