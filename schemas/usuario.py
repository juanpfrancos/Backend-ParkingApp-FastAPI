from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    id_usuario: Optional[str]
    nombre: str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str