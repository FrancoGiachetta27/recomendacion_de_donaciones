from django.db import models
from django.db.models.fields import uuid

# Create your models here.

# ===== personas vulnerables =====

class PersonaVulnerable(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    fecha_nacimiento = models.DateField()
    direccion = models.ForeignKey("Ubicacion", on_delete = models.CASCADE)
    menores_a_cargo = models.ForeignKey("self", on_delete=models.PROTECT) # no elimina las tablas referenciadas 

    class Meta: 
        db_table = 'personas_vulnerables'     
# ===== ubicaciones =====

class Ubicacion(models.Model):
    nombre = models.CharField(max_length = 40)
    latitud = models.DecimalField(max_digits = 5, decimal_places = 4)
    longitud = models.DecimalField(max_digits = 5, decimal_places = 4)
    direccion = models.ForeignKey("Direccion", on_delete=models.CASCADE)

    class Meta: 
        db_table = 'ubicaciones'     

class Direccion(models.Model):
    provincia = models.CharField(max_length = 25)
    calle = models.CharField(max_length = 30)
    altura = models.PositiveSmallIntegerField()
    
    class Meta: 
        db_table = 'direcciones'     
