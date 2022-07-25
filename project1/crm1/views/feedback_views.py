from django.shortcuts import render,redirect
from crm1.models import FeedBack, FeedBack
from crm1.forms import FeedBackForm
from django.views.generic.edit import CreateView

class FeedBackViews(CreateView):
    template_name = 'crm1/feedback_form.html'
    form_class= FeedBackForm
                
    def post(self,request):
        form = FeedBackForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                # form.save()
                uname=form.cleaned_data.get('username')
                mail = form.cleaned_data.get('email')
                pduct = form.cleaned_data.get('product')
                fback = form.cleaned_data.get('feedback')
                FeedBack.objects.create(username=uname,email=mail,product=pduct,feedback=fback)
                return redirect('crm1:thanks')
        context = {'form':form}
        return redirect('crm1/feedback_form.html',context)