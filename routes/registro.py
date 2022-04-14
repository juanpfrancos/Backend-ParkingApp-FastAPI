import imp
from fastapi import APIRouter, Response, status
from config.db import conn
from models.registro import registros
from schemas.registro import Registro
from starlette.status import HTTP_204_NO_CONTENT

registro = APIRouter()

@registro.get("/registros", response_model = list[Registro], tags=["registros"])
def get_registros():
    return conn.execute(registros.select()).fetchall()

@registro.get("/registros/{id}", response_model = Registro, tags=["registros"])
def get_registro(id: str):
    return conn.execute(registros.select().where(registros.columns.id_registro == id)).first()

@registro.put("/registros/{id}", response_model = Registro, tags=["registros"])
def update_tarifa(id: str, registro: Registro):
    conn.execute(registros.update().values(cuarto_hora = registro.cuarto_hora, hora = registro.hora, seis_horas = registro.seis_horas, dia = registro.dia, mes = registro.mes).where(registros.columns.id_registros == id))
    return conn.execute(registros.select().where(registros.columns.id_registro == id)).first()

@registro.post("/registros", response_model = Registro, tags=["registros"])
def create_registro(registro: Registro):
    nuevo_registro={"placa": registro.placa, 
                    "tipo_vehiculo": registro.tipo_vehiculo, 
                    "ingreso": registro.ingreso, 
                    "salida": registro.salida, 
                    "total_horas": registro.total_horas, 
                    "total_costo": registro.total_costo,
                    "borrado": registro.borrado,
                    "tipo_tarifa": registro.tipo_tarifa
                    }
    resultado = conn.execute(registros.insert().values(nuevo_registro))
    return conn.execute(registros.select().where(registros.columns.id_registro == resultado.lastrowid)).first()