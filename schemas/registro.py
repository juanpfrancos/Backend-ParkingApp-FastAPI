from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class Registro(BaseModel):
    id_registro: Optional[int]
    placa: str
    tipo_vehiculo: int
    ingreso: Optional[datetime]
    salida: Optional[datetime]
    total_horas: Optional[float]
    pago_inicial: Optional[float]
    pago_final: Optional[float]
    total_costo: Optional[float]
    registro_activo: Optional[bool]
    realizo: str
    tipo_tarifa: int
    en_parqueadero: Optional[bool]
    
class Ingreso(BaseModel):
    placa: str = Field(...)
    tipo_vehiculo: int = Field(...)
    realizo: int = Field(...)
    tipo_tarifa: int = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "placa": "XXX123",
                "tipo_vehiculo": "1",
                "realizo": "1",
                "tipo_tarifa": "1"
            }
        }
