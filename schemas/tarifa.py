from typing import Optional
from pydantic import BaseModel

class Tarifa(BaseModel):
    id_tarifa: Optional[int]
    cuarto_hora: float
    hora: float
    seis_horas: float
    dia: float
    mes: float