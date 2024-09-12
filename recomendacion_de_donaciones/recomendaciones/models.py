from django.db import models
from django.db.models.fields import uuid

# Create your models here.

# ===== personas vulnerables =====


class PersonaVulnerable(models.Model):
    objects: models.Manager = models.Manager()

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    direccion = models.OneToOneField("Ubicacion", on_delete=models.CASCADE)
    menores_a_cargo = models.ForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True
    )  # no elimina las tablas referenciadas

    class Meta:
        db_table = "personas_vulnerables"

    def recomendacion_para(self):
        ubicacion = Ubicacion.objects.get(id=self.direccion.id)
        direccion = Direccion.objects.get(id=ubicacion.direccion.id)
        menores_a_cargo = PersonaVulnerable.objects.all().filter(
            menores_a_cargo=self.id
        )
        cantidad_recomendada = len(menores_a_cargo)

        return dict(
            nombre=self.nombre,
            apellido=self.apellido,
            direccion=dict(
                provincia=direccion.provincia,
                calle=direccion.calle,
                altura=direccion.altura,
                latitud=ubicacion.latitud,
                longitud=ubicacion.longitud,
            ),
            cantidad_recomendada=cantidad_recomendada,
        )

    def recomendacion_para_test(self):
        ubicacion = Ubicacion.objects.get(id=self.direccion.id)
        direccion = Direccion.objects.get(id=ubicacion.direccion.id)
        menores_a_cargo = PersonaVulnerable.objects.all().filter(
            menores_a_cargo=self.id
        )
        cantidad_recomendada = len(menores_a_cargo)

        return dict(
            nombre=self.nombre,
            apellido=self.apellido,
            direccion=dict(
                provincia=direccion.provincia,
                calle=direccion.calle,
                altura=direccion.altura,
                latitud=ubicacion.latitud,
                longitud=ubicacion.longitud,
            ),
            cantidad_recomendada=cantidad_recomendada,
        )


# ===== ubicaciones =====


class Ubicacion(models.Model):
    objects: models.Manager = models.Manager()

    nombre = models.CharField(max_length=40)
    latitud = models.DecimalField(max_digits=5, decimal_places=2)
    longitud = models.DecimalField(max_digits=5, decimal_places=2)
    direccion = models.OneToOneField("Direccion", on_delete=models.CASCADE)

    class Meta:
        db_table = "ubicaciones"


class Direccion(models.Model):
    objects: models.Manager = models.Manager()

    provincia = models.CharField(max_length=25)
    calle = models.CharField(max_length=30)
    altura = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "direcciones"
