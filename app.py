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
        "name": "Vehículos",
        "description": "vehiculos routes"        
    },{
        "name": "Tarifas",
        "description": "tarifas routes"  
    },{
        "name": "Tarifas Compuestas",
        "description": "tarifasCompuestas routes"  
    },{
        "name": "Disponibilidad",
        "description": "disponibilidad routes"  
    },{
        "name": "Registros",
        "description": "registros routes"  
    },{
        "name": "Usuarios",
        "description": "registros routes"  
    }
    ]
)

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    'http://127.0.0.1:8000'
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
