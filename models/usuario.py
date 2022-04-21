from xmlrpc.client import Boolean
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine


usuarios = Table("usuarios", meta, Column(
    "id_usuario", Integer, primary_key=True), 
    Column("nombre", String(255)), 
    Column("email", String(255)),
    Column("password",String(255)),
    Column("rol",String(30)),
    Column("activo",Boolean))

meta.create_all(engine)