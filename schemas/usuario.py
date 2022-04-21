from typing import Optional
from pydantic import BaseModel, Field, EmailStr

class Usuario(BaseModel):
    id_usuario: Optional[str]
    nombre: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    rol: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "nombre": "Example",
                "email": "example@example.com",
                "password": "password",
                "rol": "rol"
            }
        }

class Login(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "email": "crhistian@example.com",
                "password": "123"
            }
        }