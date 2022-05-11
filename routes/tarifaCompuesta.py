import imp
from typing import List
from fastapi import APIRouter, Response, status
from config.db import conn
from models.tarifa import tarifas
from models.vehiculo import vehiculos
from schemas.tarifaCompuesta import TarifaCompuesta
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import select

tarifaCompuesta = APIRouter()

@tarifaCompuesta.get("/tarifasCompuestas", response_model = List[TarifaCompuesta], tags=["Tarifas Compuestas"])
def get_tarifas():
    j=vehiculos.join(tarifas, vehiculos.columns.id_vehiculo == tarifas.columns.id_tarifa)
    return conn.execute(select([vehiculos, tarifas]).select_from(j)).fetchall()