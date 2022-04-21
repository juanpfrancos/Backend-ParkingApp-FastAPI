from fastapi import Body, Depends, APIRouter, Response, status
from typing import List
from config.db import conn
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from models.usuario import usuarios
from schemas.usuario import Usuario, Login
from cryptography.fernet import Fernet
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST,  HTTP_204_NO_CONTENT
import os
from dotenv import load_dotenv
load_dotenv()

key=os.getenv('FERNET_KEY')
f = Fernet(key)

usuario = APIRouter()

@usuario.get("/usuarios", response_model = List[Usuario], tags=["Usuarios"])
def get_usuarios():
    return conn.execute(usuarios.select()).fetchall()

@usuario.get("/usuarios/{id}", response_model = Usuario, tags=["Usuarios"])
def get_usuario(id: str):
    return conn.execute(usuarios.select().where(usuarios.columns.id == id)).first()

@usuario.post("/usuarios", response_model = Usuario, tags=["Sign Up"])
def create_usuario(usuario: Usuario):
    new_user={"nombre": usuario.nombre, "email":usuario.email, "rol":usuario.rol}
    new_user["password"] = f.encrypt(usuario.password.encode("utf-8"))
    result = conn.execute(usuarios.insert().values(new_user))
    return conn.execute(usuarios.select().where(usuarios.columns.id_usuario == result.lastrowid)).first()
'''
@usuario.delete("/usuarios/{id}", status_code = status.HTTP_204_NO_CONTENT, tags=["Usuarios"])
def delete_usuario(id: str):
    conn.execute(usuarios.delete().where(usuarios.columns.id_usuario == id))
    return Response(status_code=HTTP_204_NO_CONTENT)
'''
@usuario.delete("/usuarios/{id}", status_code = status.HTTP_204_NO_CONTENT, tags=["Usuarios"], dependencies=[Depends(JWTBearer())])
def delete_usuario(id: str):
    conn.execute(usuarios.update().values(activo = 0).where(usuarios.columns.id_usuario == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@usuario.put("/usuarios/{id}", response_model = Usuario, tags=["Usuarios"], dependencies=[Depends(JWTBearer())])
def update_usuario(id: str, usuario: Usuario):
    conn.execute(usuarios.update().values(nombre = usuario.nombre, email = usuario.email, password =f.encrypt(usuario.password.encode("utf-8")), rol = usuario.rol).where(usuarios.columns.id_usuario == id))
    return conn.execute(usuarios.select().where(usuarios.columns.id_usuario==id)).first()

@usuario.post("/usuarios/login", tags=["Login"])
async def user_login(user: Login = Body(...)):
    exist_consult = conn.execute(usuarios.select().where(usuarios.columns.email == user.email)).first()
    db_rol = exist_consult[4]
    db_activo = exist_consult[5]
    if exist_consult != None and db_activo == True:
        input_pass = bytes(user.password, 'utf-8')
        pass_db = bytes(exist_consult[3], 'utf-8')
        db_decrypted = f.decrypt(pass_db)
        if input_pass == db_decrypted and db_rol == 'operario':
            print('Logueado operario')
            return signJWT(user.email, db_rol)
        elif input_pass == db_decrypted and db_rol == 'administrador':
            print('Logueado administrador')
            return signJWT(user.email, db_rol)
        else:
            print('PassIncorrect')
            return Response(status_code=400)
    else:
        print('usuario inexistente')
        return {"error": "Wrong login details!"}
