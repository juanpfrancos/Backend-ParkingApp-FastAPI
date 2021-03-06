import imp
from typing import List
from fastapi import APIRouter, Response, status
from config.db import conn
from models.tarifa import tarifas
from schemas.tarifa import Tarifa
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import join, select

tarifa = APIRouter()

@tarifa.get("/tarifas", response_model = List[Tarifa], tags=["Tarifas"])
def get_tarifas():
    return conn.execute(tarifas.select()).fetchall()

@tarifa.get("/tarifas/{id}", response_model = Tarifa, tags=["Tarifas"])
async def get_tarifa(id: int):
    return conn.execute(tarifas.select().where(tarifas.columns.id_tarifa == id)).first()

@tarifa.put("/tarifas/{id}", response_model = Tarifa, tags=["Tarifas"])
async def update_tarifa(id: str, tarifa: Tarifa):
    conn.execute(tarifas.update().values(cuarto_hora = tarifa.cuarto_hora, hora = tarifa.hora, seis_horas = tarifa.seis_horas, dia = tarifa.dia, mes = tarifa.mes).where(tarifas.columns.id_tarifa == id))
    return conn.execute(tarifas.select().where(tarifas.columns.id_tarifa == id)).first()