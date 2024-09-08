from typing import Optional

from ninja import Schema


class DireccionSchema(Schema):
    provincia: Optional[str]
    calle: str
    altura: Optional[int] = None


class CoordenadaSchema(Schema):
    latitud: float
    longitud: float


class Recomendacion(Schema):
    pass
