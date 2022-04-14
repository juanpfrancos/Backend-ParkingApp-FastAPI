from fastapi import APIRouter, Response, status
from config.db import conn
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

@usuario.get("/usuarios", response_model = list[Usuario], tags=["usuarios"])
def get_usuarios():
    return conn.execute(usuarios.select()).fetchall()

@usuario.get("/usuarios/{id}", response_model = Usuario, tags=["usuarios"])
def get_usuario(id: str):
    return conn.execute(usuarios.select().where(usuarios.columns.id == id)).first()

@usuario.post("/usuarios", response_model = Usuario, tags=["Sign Up"])
def create_usuario(usuario: Usuario):
    new_user={"nombre": usuario.nombre, "email":usuario.email}
    new_user["password"] = f.encrypt(usuario.password.encode("utf-8"))
    result = conn.execute(usuarios.insert().values(new_user))
    return conn.execute(usuarios.select().where(usuarios.columns.id_usuario == result.lastrowid)).first()

@usuario.delete("/usuarios/{id}", status_code = status.HTTP_204_NO_CONTENT, tags=["usuarios"])
def delete_usuario(id: str):
    conn.execute(usuarios.delete().where(usuarios.columns.id_usuario == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@usuario.put("/usuarios/{id}", response_model = Usuario, tags=["usuarios"])
def update_usuario(id: str, usuario: Usuario):
    conn.execute(usuarios.update().values(nombre = usuario.nombre, email = usuario.email, password =f.encrypt(usuario.password.encode("utf-8"))).where(usuarios.columns.id == id))
    return conn.execute(usuarios.select().where(usuarios.columns.id_usuario==id)).first()


@usuario.post("/validar-login",  tags=["Login"])
def create_usuario(usuario: Login):
    exist_email = conn.execute(usuarios.select().where(usuarios.columns.email == usuario.email)).first()

    if exist_email != None:
        input_pass = bytes(usuario.password, 'utf-8')
        pass_db = bytes(exist_email[3], 'utf-8')
        db_decrypted = f.decrypt(pass_db)
        if input_pass == db_decrypted:
            print('Logueado')
            return Response(status_code=HTTP_200_OK)
        else:
            print('PassIncorrect')
            return Response(status_code=HTTP_400_BAD_REQUEST)
    else:
        print('usuario inexistente')
        return Response(status_code=HTTP_400_BAD_REQUEST)
