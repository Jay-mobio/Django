from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from requests import request
from crm1.models import Customer
from django.http import Http404
from crm1.filters import CustomerFilter



class CustomertListViews(ListView):
    model = Customer
    template_name_suffix = '_list_view'
    context_object_name = 'customers'
    ordering = ['id']
    paginate_by = 2
    # paginate_by = 4
    paginate_orphans = 2


    def get(self,request): 
        data = Customer.objects.all()
        if 'search' in request.GET:
            search = request.GET['search']
            print(search,'------------------------')
            
            data = Customer.objects.filter(name__icontains=search)
        else:
            data = Customer.objects.all() 
        



        filter_form = CustomerFilter(request.GET, queryset=Customer.objects.all())
        context = {'data':data, 'filter_form':filter_form}
        return render(request,'crm1/customer_list_view.html',context)
        
        
    #     if 'q' in request.GET:
    #         q = request.GET['q']
            # data = Customer.objects.filter(name__icontains=q)
        # else:
        #     data = Customer.objects.all()        

        # context = {'data': data}
        # return render(request, 'crm1/customer_list_view.html', context)

    # def get_context_data(self,*args, **kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     context["freshers"] = Customer.objects.all().order_by('name')
    #     return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user']=='jay1':
    #         template_name = 'crm1/jay1.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]

    # def get_paginate_by(self,*args,**kwargs):
    #     try:
    #         return super(CustomertListViews,self).get_paginate_by(*args,**kwargs)
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         return super(CustomertListViews,self).get_paginate_by(*args,**kwargs)   
    


# data = data.objects.all()

# if q in ___ :
#     data.search()

# if filter in __:
#     data.filter()

# return data

