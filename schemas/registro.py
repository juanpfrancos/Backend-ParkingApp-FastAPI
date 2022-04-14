from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Registro(BaseModel):
    id_registro: Optional[str]
    placa: str
    tipo_vehiculo: int
    ingreso: datetime
    salida: Optional[datetime]
    total_horas: Optional[float]
    total_costo: Optional[float]
    borrado: bool
    tipo_tarifa: int