from rest_framework import serializers
from . import models

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Almacen
        fields = '__all__'