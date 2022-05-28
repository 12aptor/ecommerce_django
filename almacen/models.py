from django.db import models

# Create your models here.

class Almacen(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
