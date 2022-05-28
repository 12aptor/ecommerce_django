from dataclasses import fields
from rest_framework import serializers
from . import models

class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pagos
        fields = '__all__'