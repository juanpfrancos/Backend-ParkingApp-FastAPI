from pydantic import BaseModel

class Disponibilidad(BaseModel):
    capacidad: int
    ocupados: int