from fastapi import FastAPI
from routes.usuario import usuario
from routes.vehiculo import vehiculo
from routes.tarifa import tarifa
from routes.tarifaCompuesta import tarifaCompuesta
from routes.registro import registro
from routes.disponibilidad import disponibilidad

app = FastAPI(
    title="Parking APP API",
    description="Desarrollado por Christian Arenas y Juan Pablo Franco",
    openapi_tags=[
    {
        "name": "users",
        "description": "users routes"
    },{
        "name": "vehiculos",
        "description": "vehiculos routes"        
    },{
        "name": "tarifas",
        "description": "tarifas routes"  
    },{
        "name": "tarifasCompuestas",
        "description": "tarifasCompuestas routes"  
    },{
        "name": "disponibilidad",
        "description": "disponibilidad routes"  
    },{
        "name": "registros",
        "description": "registros routes"  
    }
    ]
)

app.include_router(usuario)
app.include_router(vehiculo)
app.include_router(tarifa)
app.include_router(tarifaCompuesta)
app.include_router(registro)
app.include_router(disponibilidad)
