from django.shortcuts import render

from django.views.generic.base import View

class home(View):
    def get(self,request):
        return (request,'dashboard.html')