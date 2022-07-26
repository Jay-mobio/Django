import django_filters as filter
from crm1.models import Customer

class Age_Filter(filter.FilterSet):

    class Meta:
        model = Customer
        fields = ['']