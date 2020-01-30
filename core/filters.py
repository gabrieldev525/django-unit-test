# django imports
import django_filters

# third imports

# local imports
from .models import Register

class RegisterFilterSet(django_filters.FilterSet):

    class Meta:
        model = Register
        fields = '__all__'
