from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models

# Create your views here.


class AlmacenView(generics.CreateAPIView):

    queryset = models.Almacen.objects.all()
    serializer_class = serializers.AlmacenSerializer