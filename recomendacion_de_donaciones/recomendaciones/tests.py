from django.test import TestCase
from recomendacion_de_donaciones.recomendaciones.models import (
    Direccion,
    PersonaVulnerable,
    Ubicacion,
)


# Create your tests here.
class RecomendacionesTest(TestCase):
    def set_up():
        Direccion.objects.create(calle="Urquiza", altura=200, provincia="Santa Fe")
        Direccion.objects.create(
            calle="Hipólito Yrigoyen", altura=300, provincia="Cordoba"
        )
        Direccion.objects.create(calle="Beltrán", altura=100, provincia="Mendoza")
        Direccion.objects.create(calle="Paraguay ", altura=90, provincia="Corrientes")
        Direccion.objects.create(
            calle="Corrientes ", altura=700, provincia="Buenos Aires"
        )
        Direccion.objects.create(calle="25 de Mayo", altura=450, provincia="Entre Rios")
        Direccion.objects.create(calle="Medrano", altura=22, provincia="Buenos Aires")
        Direccion.objects.create(
            calle="Juan B Justo", altura=22, provincia="Buenos Aires"
        )
        Direccion.objects.create(
            calle="Directorio", altura=532, provincia="Buenos Aires"
        )
        Direccion.objects.create(calle="Acoyte", altura=1099, provincia="Buenos Aires")

        Ubicacion.objects.create(
            nombre="ubcacion1",
            latitud=-33.15,
            longitud=-60.49,
            calle="Urquiza",
            altura=200,
        )
        Ubicacion.objects.create(
            nombre="ubcacion2",
            latitud=-33.12,
            longitud=-64.34,
            calle="Hipólito Yrigoyen",
            altura=300,
        )
        Ubicacion.objects.create(
            nombre="ubcacion3",
            latitud=-32.92,
            longitud=-68.84,
            calle="Beltrán",
            altura=100,
        )
        Ubicacion.objects.create(
            nombre="ubcacion4",
            latitud=-29.13,
            longitud=-59.25,
            calle="Paraguay ",
            altura=90,
        )
        Ubicacion.objects.create(
            nombre="ubcacion5",
            latitud=-38.71,
            longitud=-62.25,
            calle="Corrientes ",
            altura=700,
        )
        Ubicacion.objects.create(
            nombre="ubcacion6",
            latitud=-31.62,
            longitud=-58.50,
            calle="25 de Mayo",
            altura=450,
        )
        Ubicacion.objects.create(
            nombre="ubcacion7",
            latitud=-33.80,
            longitud=-59.51,
            calle="Medrano",
            altura=22,
        )
        Ubicacion.objects.create(
            nombre="ubcacion8",
            latitud=-34.43,
            longitud=-61.82,
            calle="Juan B Justo",
            altura=22,
        )
        Ubicacion.objects.create(
            nombre="ubcacion9",
            latitud=-34.66,
            longitud=-58.41,
            calle="Directorio",
            altura=532,
        )
        Ubicacion.objects.create(
            nombre="ubcacion10",
            latitud=-34.60,
            longitud=-58.44,
            calle="Acoyte",
            altura=1099,
        )

        PersonaVulnerable.objects.create(
            nombre="federico",
            apellido="Urquiza",
            fecha_nacimiento="2002-11-08",
            direccion=1,
        )
        PersonaVulnerable.objects.create(
            nombre="santiago",
            apellido="Urquiza",
            fecha_nacimiento="2003-04-04",
            direccion=2,
        )
        PersonaVulnerable.objects.create(
            nombre="marcos",
            apellido="Urquiza",
            fecha_nacimiento="2003-06-26",
            direccion=3,
        )
        PersonaVulnerable.objects.create(
            nombre="elina",
            apellido="Urquiza",
            fecha_nacimiento="2002-11-20",
            direccion=4,
        )
        PersonaVulnerable.objects.create(
            nombre="sofia",
            apellido="Urquiza",
            fecha_nacimiento="2002-11-21",
            direccion=5,
        )
        PersonaVulnerable.objects.create(
            nombre="manuel",
            apellido="Urquiza",
            fecha_nacimiento="2003-05-03",
            direccion=6,
        )
        PersonaVulnerable.objects.create(
            nombre="delfina",
            apellido="Urquiza",
            fecha_nacimiento="2003-05-07",
            direccion=7,
        )
        PersonaVulnerable.objects.create(
            nombre="nicolas",
            apellido="Urquiza",
            fecha_nacimiento="2003-01-05",
            direccion=8,
        )
        PersonaVulnerable.objects.create(
            nombre="pepe",
            apellido="Urquiza",
            fecha_nacimiento="2002-12-02",
            direccion=9,
        )
        PersonaVulnerable.objects.create(
            nombre="fiona",
            apellido="Urquiza",
            fecha_nacimiento="2002-05-27",
            direccion=10,
        )

    def test_recomendaciones():
        lat = -32.855153049454
        lon = -60.6976005574217

        personas_vulnerables = PersonaVulnerable.objects.raw(
            f"""
                select  from personas_vulnerables pv
                join ubicaciones ub on pv.direccion_id = ub.id
                where sqrt(pow(ub.latitud - {lat}, 2) + pow(ub.longitud - {lon}, 2)) < {2}
                limit {5}
            """
        )
        recomendaciones = map(lambda p: p.recomendacion_para(), personas_vulnerables)

        expected = [
            dict(
                nombre="federico",
                apellido="Urquiza",
                direccion=dict(
                    provincia="Santa Fe",
                    calle="Urquiza",
                    altura=200,
                    latitud=-33.15,
                    longitud=-60.49,
                ),
            ),
            dict(
                nombre="delfina",
                apellido="Urquiza",
                direccion=dict(
                    provincia="Santa Fe",
                    latitud=-33.80,
                    longitud=-59.51,
                    calle="Medrano",
                    altura=22,
                ),
            ),
            dict(
                nombre="federico",
                apellido="Urquiza",
                direccion=dict(
                    provincia="Santa Fe",
                    calle="Urquiza",
                    altura=200,
                    latitud=-33.15,
                    longitud=-60.49,
                ),
            ),
        ]
