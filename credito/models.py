from django.db import models

# Create your models here.


class Pagos(models.Model):
    cantidad = models.IntegerField()