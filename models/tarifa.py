from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine


tarifas = Table("tarifas", meta, 
    Column("id_tarifa", Integer, primary_key=True), 
    Column("cuarto_hora", Numeric(8)),
    Column("hora", Numeric(8)),
    Column("seis_horas", Numeric(8)),
    Column("dia", Numeric(8)),
    Column("mes", Numeric(8))
)

meta.create_all(engine)