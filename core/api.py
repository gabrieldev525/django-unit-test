# third imports
from rest_framework import viewsets
from rest_framework import routers
from rest_framework.decorators import action

# local imports
from .models import Register
from .serializers import RegisterSerializers

class RegisterViewSet(viewsets.ModelViewSet):
    model = Register
    queryset = Register.objects.all()
    serializer_class = RegisterSerializers


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'register', RegisterViewSet, 'register')

urlpatterns = router.urls