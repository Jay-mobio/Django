from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from crm1.models import Customer
from django.http import Http404

class CustomertListViews(ListView):
    model = Customer
    template_name_suffix = '_detail_list'
    context_object_name = 'customers'
    ordering = ['name']
    # paginate_by = 2
    # paginate_by = 4
    # paginate_orphans = 2

    def get(self,request):
        if 'q' in request.GET:
            q = request.GET['q']
            data = Customer.objects.filter(name__icontains=q)
        else:
            data = Customer.objects.all()
        context = {'data': data}
        return render(request, 'crm1/customer_detail_list.html', context)

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
    #         return super(CustomertDeailViews,self).get_paginate_by(*args,**kwargs)
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         return super(CustomertDeailViews,self).get_paginate_by(*args,**kwargs)   
    
