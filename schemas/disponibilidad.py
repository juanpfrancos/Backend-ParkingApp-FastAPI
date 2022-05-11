from pydantic import BaseModel

class Disponibilidad(BaseModel):
    disponibles: int
    ocupados: int