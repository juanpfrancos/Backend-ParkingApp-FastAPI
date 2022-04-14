from typing import Optional
from pydantic import BaseModel

class TarifaCompuesta(BaseModel):
    id_vehiculo: Optional[str]
    tipo_vehiculo: str
    cuarto_hora: float
    hora: float
    seis_horas: float
    dia: float
    mes: float