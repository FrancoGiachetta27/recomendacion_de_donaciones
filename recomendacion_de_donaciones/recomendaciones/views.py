# Create your views here.

from requests.api import _HeadersMapping
from typing_extensions import List
import requests
from ninja import NinjaAPI
from .schemas import DireccionSchema, CoordenadaSchema, Recomendacion

GEOREF = "https://apis.datos.gob.ar/georef/api"

api = NinjaAPI()


@api.get("/recomendaciones", response=List[Recomendacion])
def recomandacion_direccion(
    request, direccion_parm: DireccionSchema, max_parm: int = 5
):
    params = dict(
        direccion=direccion_parm.calle,
        provincia=direccion_parm.provincia,
        max=max_parm,
    )

    georef_response = requests.get(GEOREF + "/direcciones", params=params)


@api.get("/recomendaciones", response=List[Recomendacion])
def recomandacion_coordenadas(request, coordenda: CoordenadaSchema, max: int):
    pass
