from django.test import TestCase
from .models import (
    Direccion,
    PersonaVulnerable,
    Ubicacion,
)


# Create your tests here.
class RecomendacionesTest(TestCase):
    def setUp(self):
        d1 = Direccion.objects.create(calle="Urquiza", altura=200, provincia="Santa Fe")
        d2 = Direccion.objects.create(
            calle="Hipólito Yrigoyen", altura=300, provincia="Cordoba"
        )
        d3 = Direccion.objects.create(calle="Beltrán", altura=100, provincia="Mendoza")
        d4 =Direccion.objects.create(calle="Paraguay ", altura=90, provincia="Corrientes")
        d5 =Direccion.objects.create(
            calle="Corrientes ", altura=700, provincia="Buenos Aires"
        )
        d6 =Direccion.objects.create(calle="25 de Mayo", altura=450, provincia="Entre Rios")
        d7 =Direccion.objects.create(calle="Medrano", altura=22, provincia="Buenos Aires")
        d8 =Direccion.objects.create(
            calle="Juan B Justo", altura=22, provincia="Buenos Aires"
        )
        d9 =Direccion.objects.create(
            calle="Directorio", altura=532, provincia="Buenos Aires"
        )
        d10 =Direccion.objects.create(calle="Acoyte", altura=1099, provincia="Buenos Aires")

        u1 = Ubicacion.objects.create(
            nombre="ubcacion1",
            latitud=-33.15,
            longitud=-60.49,
            direccion=d1
        )
        u2 = Ubicacion.objects.create(
            nombre="ubcacion2",
            latitud=-33.12,
            longitud=-64.34,
            direccion=d2
        )
        u3 = Ubicacion.objects.create(
            nombre="ubcacion3",
            latitud=-32.92,
            longitud=-68.84,
            direccion=d3
        )
        u4 = Ubicacion.objects.create(
            nombre="ubcacion4",
            latitud=-29.13,
            longitud=-59.25,
            direccion=d4
        )
        u5 = Ubicacion.objects.create(
            nombre="ubcacion5",
            latitud=-38.71,
            longitud=-62.25,
            direccion=d5
        )
        u6 = Ubicacion.objects.create(
            nombre="ubcacion6",
            latitud=-31.62,
            longitud=-58.50,
            direccion=d6
        )
        u7 = Ubicacion.objects.create(
            nombre="ubcacion7",
            latitud=-33.80,
            longitud=-59.51,
            direccion=d7
        )
        u8 = Ubicacion.objects.create(
            nombre="ubcacion8",
            latitud=-34.43,
            longitud=-61.82,
            direccion=d8
        )
        u9 = Ubicacion.objects.create(
            nombre="ubcacion9",
            latitud=-34.66,
            longitud=-58.41,
            direccion=d9
        )
        u10 = Ubicacion.objects.create(
            nombre="ubcacion10",
            latitud=-34.60,
            longitud=-58.44,
            direccion=d10
        )

        PersonaVulnerable.objects.create(
            nombre="federico",
            apellido="Urquiza",
            fecha_nacimiento="2002-11-08",
            direccion=u1,
        )
        PersonaVulnerable.objects.create(
            nombre="santiago",
            apellido="Urquiza",
            fecha_nacimiento="2003-04-04",
            direccion=u2,
        )
        PersonaVulnerable.objects.create(
            nombre="marcos",
            apellido="Urquiza",
            fecha_nacimiento="2003-06-26",
            direccion=u3,
        )
        PersonaVulnerable.objects.create(
            nombre="elina",
            apellido="Urquiza",
            fecha_nacimiento="2002-11-20",
            direccion=u4,
        )
        PersonaVulnerable.objects.create(
            nombre="sofia",
            apellido="Urquiza",
            fecha_nacimiento="2002-11-21",
            direccion=u5,
        )
        PersonaVulnerable.objects.create(
            nombre="manuel",
            apellido="Urquiza",
            fecha_nacimiento="2003-05-03",
            direccion=u6,
        )
        PersonaVulnerable.objects.create(
            nombre="delfina",
            apellido="Urquiza",
            fecha_nacimiento="2003-05-07",
            direccion=u7,
        )
        PersonaVulnerable.objects.create(
            nombre="nicolas",
            apellido="Urquiza",
            fecha_nacimiento="2003-01-05",
            direccion=u8,
        )
        PersonaVulnerable.objects.create(
            nombre="pepe",
            apellido="Urquiza",
            fecha_nacimiento="2002-12-02",
            direccion=u9,
        )
        PersonaVulnerable.objects.create(
            nombre="fiona",
            apellido="Urquiza",
            fecha_nacimiento="2002-05-27",
            direccion=u10,
        )

    def test_recomendaciones(self):
        lat = -32.855153049454
        lon = -60.6976005574217

        personas_vulnerables = PersonaVulnerable.objects.raw(
            f"""
                select * from personas_vulnerables pv
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
                    provincia="Buenos Aires",
                    calle="Medrano",
                    altura=22,
                    latitud=-33.80,
                    longitud=-59.51,
                ),
            ),
            dict(
                nombre="nicolas",
                apellido="Urquiza",
                direccion=dict(
                    provincia="Buenos Aires",
                    calle="Juan B Justo",
                    altura=22,
                    latitud=-34.43,
                    longitud=-61.82,
                ),
            ),
        ]

        self.assertEqual(list(recomendaciones), expected)
