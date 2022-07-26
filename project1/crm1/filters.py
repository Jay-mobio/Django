import django_filters

from crm1.models import Customer

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['name','phone','age','email']