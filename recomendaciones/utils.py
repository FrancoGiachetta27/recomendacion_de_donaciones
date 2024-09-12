from typing_extensions import Dict
import requests
from math import asin, cos, pi, asin, sqrt

GEOREF = "https://apis.datos.gob.ar/georef/api/"


def georef_request_coords(endpoint: str, params) -> Dict[str, float]:
    url = GEOREF + f"{endpoint}"
    georef = requests.get(url=url, params=params).json()
    ubicacion = georef["direcciones"][0]["ubicacion"]
    result = dict(
        latitud=ubicacion["lat"],
        longitud=ubicacion["lon"],
    )

    return result

# dadas dos coordenadas, calcula la distanta entre dos puntos en la tierra usando la formula de haversine 
def distancia_coordenadas(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    radio = 6371  # km
    pi_grados = pi / 180

    a = (
        0.5
        - cos((lat2 - lat1) * pi_grados) / 2
        + cos(lat1 * pi_grados) * cos(lat2 * pi_grados) * (1 - cos((lon2 - lon1) * pi_grados)) / 2
    )
    return 2 * radio * asin(sqrt(a))
