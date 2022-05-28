from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.


class PostPagosView(generics.CreateAPIView):
    queryset = models.Pagos.objects.all()
    serializer_class = serializers.PagosSerializer

class GetPagosView(generics.ListAPIView):
    queryset = models.Pagos.objects.all()
    serializer_class = serializers.PagosSerializer