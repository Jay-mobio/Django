from django.shortcuts import render
from crm1.models import Customer
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class CustomerDetailViews(DetailView):
    model = Customer
    context_object_name = 'cost'

    def get_context_data(self, **kwargs):
        context = super.get_context_data(self, **kwargs)
        context['all_customer'] = self.model.objects.all()
        return super().get_context_data(**kwargs)
  
class CustomerList(ListView):
    model = Customer
    template_name_suffix = "_detail_list"