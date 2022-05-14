import imp
from typing import List
from fastapi import APIRouter, Response, status
from config.db import conn
from models.registro import registros
from models.usuario import usuarios
from models.vehiculo import vehiculos
from schemas.registro import Registro, Ingreso, RegistroGet
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import select

registro = APIRouter()

@registro.get("/registros/{io}", response_model = List[RegistroGet], tags=["Registros"])
async def get_registros(io: bool):
    j=registros.join(usuarios, registros.columns.realizo == usuarios.columns.id_usuario).join(vehiculos, registros.columns.tipo_vehiculo == vehiculos.columns.id_vehiculo)
    return conn.execute(select([usuarios, registros, vehiculos]).select_from(j).where((registros.columns.en_parqueadero == io) & (registros.columns.registro_activo == '1'))).fetchall()

@registro.get("/registros/{id}", response_model = Registro, tags=["Registros"])
async def get_registro(id: int):
    return conn.execute(registros.select().where(registros.columns.id_registro == id)).first()

@registro.post("/registros", response_model = Ingreso, tags=["Registros"])
async def ingresar_vehiculo(ingreso: Ingreso):
    nuevo_ingreso={"placa": ingreso.placa, 
                    "tipo_vehiculo": ingreso.tipo_vehiculo,
                    "realizo": ingreso.realizo,
                    "tipo_tarifa": ingreso.tipo_tarifa
                    }
    resultado = conn.execute(registros.insert().values(nuevo_ingreso))
    return conn.execute(registros.select().where(registros.columns.id_registro == resultado.lastrowid)).first()

@registro.put("/registros/{id}", response_model = Registro, tags=["Registros"])
async def sacar_vehiculo(id: int):
    conn.execute(registros.update().values(en_parqueadero = 0).where(registros.columns.id_registro == id))
    return conn.execute(registros.select().where(registros.columns.id_registro == id)).first()

@registro.delete("/registros/{id}", response_model = Registro, tags=["Registros"])
async def delete_registro(id: int):
    conn.execute(registros.update().values(registro_activo = 0).where(registros.columns.id_registro == id))
    return Response(status_code=HTTP_204_NO_CONTENT)