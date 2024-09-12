# Create your views here.

from typing_extensions import Dict, List, Optional
from ninja import NinjaAPI


from .models import PersonaVulnerable
from .schemas import DireccionSchema, RecomendacionPersonaVulnerable
from .utils import distancia_coordenadas, georef_request_coords

api = NinjaAPI()


@api.get("/recomendaciones", response=List[RecomendacionPersonaVulnerable])
def recomandacion_direccion(
    request,
    calle: str,
    altura: int,
    provincia: Optional[str],
    radio_max: int,
    max_parm: int = 5,
):
    params = dict(direccion=calle + str(altura), provincia=provincia, max=1)

    georef_response = georef_request_coords("direcciones", params)
    
    personas_vulnerables = PersonaVulnerable.objects.raw(
        f"""
            select * from personas_vulnerables pv
            join ubicaciones ub on pv.direccion_id = ub.id
            where pow(ub.latitud - {georef_response["latitud"]}, 2) + pow(ub.longitud - {georef_response["longitud"]}, 2) < {radio_max}
            limit {max_parm}
        """
    )
    recomendaciones = map(lambda p: p.recomendacion_para(), personas_vulnerables)

    return list(recomendaciones)


# @api.get("/recomendaciones", response=List[RecomendacionPersonaVulnerable])
# def recomandacion_coordenadas(request, coordenda: CoordenadaSchema, max: int):
#     pass
