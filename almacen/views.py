from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models

# Create your views here.


class PostAlmacenView(generics.CreateAPIView):

    queryset = models.Almacen.objects.all()
    serializer_class = serializers.AlmacenSerializer

class GetAlmacenView(generics.ListAPIView):
    queryset = models.Almacen.objects.all()
    serializer_class = serializers.AlmacenSerializer