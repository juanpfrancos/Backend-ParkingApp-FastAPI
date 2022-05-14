from pydantic import BaseModel

class Tarifa(BaseModel):
    cuarto_hora: float
    hora: float
    seis_horas: float
    dia: float
    mes: float