# third imports
from rest_framework import serializers

# local imports
from .models import Register

class RegisterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = '__all__'