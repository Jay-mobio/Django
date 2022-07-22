from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib import messages
from crm1.forms import UserRegister
from django.contrib.auth.models import User

class RegisterView(CreateView):
    title = ("Register Page")
    template_name = 'crm1/register.html' 
    form_class = UserRegister

    def post(self,request):
        if request.user.is_authenticated:
            return redirect('crm1:login')
        else:
            form = UserRegister
            if request.method == 'POST':
                form = UserRegister(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    # group = Group.objects.get(name='customer')
                    # user.groups.add(group)                    
                    messages.success(request, 'Account was created for' +username)
                    return redirect('crm1:home')

            context = {'form':form}
            return render(request,'crm1/register.html',context)
    