from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine


vehiculos = Table("vehiculos", meta, 
    Column("id_vehiculo", Integer, primary_key=True), 
    Column("nombre_vehiculo", String(15)),
    Column("capacidad", Integer))
meta.create_all(engine)
