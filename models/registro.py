from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine


registros = Table("registros", meta, 
    Column("id_registro", Integer, primary_key=True), 
    Column("placa", String(8)),
    Column("tipo_vehiculo", Integer),
    Column("ingreso", DateTime),
    Column("salida", DateTime),
    Column("total_horas", Numeric(8)),
    Column("total_costo", Numeric(8)),
    Column("activo", Boolean),
    Column("tipo_tarifa", Integer)
)

meta.create_all(engine)