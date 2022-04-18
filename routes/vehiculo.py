import imp
from fastapi import APIRouter, Response, status
from config.db import conn
from models.vehiculo import vehiculos
from schemas.vehiculo import Vehiculo
from starlette.status import HTTP_204_NO_CONTENT

vehiculo = APIRouter()

@vehiculo.get("/vehiculos", tags=["Vehículos"])
def get_vehiculos():
    return conn.execute(vehiculos.select()).fetchall()

@vehiculo.get("/vehiculos/{id}", response_model = Vehiculo, tags=["Vehículos"])
def get_vehiculo(id: str):
    return conn.execute(vehiculos.select().where(vehiculos.columns.id_vehiculo == id)).first()