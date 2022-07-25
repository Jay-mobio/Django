from django.shortcuts import render
from django.views.generic.base import TemplateView


class ThanksViews(TemplateView):
    def get(self,request):
        return render(request,'crm1/thanks.html')
