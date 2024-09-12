from typing import Optional

from ninja import Schema

from .models import PersonaVulnerable, Ubicacion


class DireccionSchema(Schema):
    provincia: Optional[str]
    calle: str
    altura: Optional[int] = None
    latitud: float
    longitud: float


class RecomendacionPersonaVulnerable(Schema):
    nombre: str
    apellido: str
    direccion: DireccionSchema
    cantidad_recomendada: int

    @staticmethod
    def from_persona_vulnerable(persona_vulnerable: PersonaVulnerable):
        direccion = Ubicacion.objects.get(id=persona_vulnerable.direccion.id)
        menores_a_cargo = PersonaVulnerable.objects.all().filter(
            menores_a_cargo=persona_vulnerable.id
        )
        cantidad_recomendada = len(menores_a_cargo)

        return RecomendacionPersonaVulnerable(
            nombre=persona_vulnerable.nombre,
            apellido=persona_vulnerable.apellido,
            direccion=direccion,
            cantidad_recomendada=cantidad_recomendada,
        )
