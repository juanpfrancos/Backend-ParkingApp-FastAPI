import imp
from typing import List
from fastapi import APIRouter, Response, status
from config.db import conn
from models.registro import registros
from schemas.registro import Registro, Ingreso
from starlette.status import HTTP_204_NO_CONTENT

registro = APIRouter()

@registro.get("/registros", response_model = List[Registro], tags=["Registros"])
def get_registros():
    return conn.execute(registros.select()).fetchall()

@registro.get("/registros/{id}", response_model = Registro, tags=["Registros"])
def get_registro(id: int):
    return conn.execute(registros.select().where(registros.columns.id_registro == id)).first()

@registro.post("/registros", response_model = Ingreso, tags=["Registros"])
def ingresar_vehiculo(ingreso: Ingreso):
    nuevo_ingreso={"placa": ingreso.placa, 
                    "tipo_vehiculo": ingreso.tipo_vehiculo,
                    "realizo": ingreso.realizo,
                    "tipo_tarifa": ingreso.tipo_tarifa
                    }
    resultado = conn.execute(registros.insert().values(nuevo_ingreso))
    return conn.execute(registros.select().where(registros.columns.id_registro == resultado.lastrowid)).first()

@registro.put("/registros/{id}", response_model = Registro, tags=["Registros"])
def sacar_vehiculo(id: int):
    conn.execute(registros.update().values(en_parqueadero = 0).where(registros.columns.id_registro == id))
    return conn.execute(registros.select().where(registros.columns.id_registro == id)).first()

@registro.delete("/registros/{id}", response_model = Registro, tags=["Registros"])
def delete_registro(id: int):
    conn.execute(registros.update().values(registro_activo = 0).where(registros.columns.id_registro == id))
    return Response(status_code=HTTP_204_NO_CONTENT)