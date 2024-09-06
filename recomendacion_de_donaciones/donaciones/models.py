from django.db import models

# Create your models here.

class Ubicacion(models.Model):
    latitud = models.DecimalField(max_digits=4)
    longitud = models.DecimalField(max_digits=4)
