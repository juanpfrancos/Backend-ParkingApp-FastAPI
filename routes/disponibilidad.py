import imp
from itertools import count
from fastapi import APIRouter, Response, status
from config.db import conn
from models.registro import registros
from models.vehiculo import vehiculos
from schemas.disponibilidad import Disponibilidad
from starlette.status import HTTP_400_BAD_REQUEST
from sqlalchemy import select, func, subquery

disponibilidad = APIRouter()

@disponibilidad.get("/disponibilidad/{tipo_vehiculo}/{tipo_tarifa}", response_model = Disponibilidad, tags=["Disponibilidad"])
async def get_disponibilidad(tipo_vehiculo: int, tipo_tarifa: int):
    if tipo_tarifa == 1 or tipo_tarifa == 2 or tipo_tarifa == 3:
        return conn.execute(select((vehiculos.columns.capacidad/2).label('capacidad'), ((select(func.count()).select_from(registros).where((registros.columns.tipo_vehiculo == tipo_vehiculo) & (registros.columns.registro_activo == '1') & (registros.columns.en_parqueadero == '1') & (registros.columns.tipo_tarifa == tipo_tarifa)))).label('ocupados')).select_from(vehiculos).where(vehiculos.columns.id_vehiculo == tipo_vehiculo)).first()
    elif tipo_tarifa == 4:
        return conn.execute(select((vehiculos.columns.capacidad/2).label('capacidad'), ((select(func.count()).select_from(registros).where((registros.columns.tipo_vehiculo == tipo_vehiculo) & (registros.columns.registro_activo == '1') & (registros.columns.en_parqueadero == '1') & (registros.columns.tipo_tarifa == tipo_tarifa)))).label('ocupados')).select_from(vehiculos).where(vehiculos.columns.id_vehiculo == tipo_vehiculo)).first()
    else:
        return Response(status_code=HTTP_400_BAD_REQUEST)