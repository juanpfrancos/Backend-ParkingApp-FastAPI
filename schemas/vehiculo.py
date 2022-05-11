from typing import Optional
from pydantic import BaseModel

class Vehiculo(BaseModel):
    id_vehiculo: Optional[int]
    nombre_vehiculo: str
    capacidad: int