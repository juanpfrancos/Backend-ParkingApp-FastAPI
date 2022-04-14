import imp
from itertools import count
from fastapi import APIRouter, Response, status
from config.db import conn
from models.registro import registros
from schemas.disponibilidad import Disponibilidad
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import select, func

disponibilidad = APIRouter()

@disponibilidad.get("/disponibilidad/{id}", response_model = Disponibilidad, tags=["disponibilidad"])
def get_disponibilidad(id: str):
    return conn.execute(select(func.count().label('total_cupo')).select_from(registros).where((registros.columns.tipo_vehiculo == id) & (registros.columns.borrado == '0') & (registros.columns.total_costo == None))).first()
