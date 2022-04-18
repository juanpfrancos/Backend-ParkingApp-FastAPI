from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

origins = [
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario)
app.include_router(vehiculo)
app.include_router(tarifa)
app.include_router(tarifaCompuesta)
app.include_router(registro)
app.include_router(disponibilidad)
