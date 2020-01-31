# third imports
from rest_framework import viewsets
from rest_framework import routers
from rest_framework import filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

# local imports
from .models import Register
from .serializers import RegisterSerializers
from .filters import RegisterFilterSet


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name', 'desc')
    filter_class = RegisterFilterSet
    permission_classes = [IsAdminUser, IsAuthenticated]


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'register', RegisterViewSet, 'register')

urlpatterns = router.urls