from typing import Optional
from pydantic import BaseModel

class Vehiculo(BaseModel):
    id_vehiculo: Optional[str]
    tipo_vehiculo: str