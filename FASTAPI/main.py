from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from middlewares import BearerJWT

app = FastAPI(
    title="Mi primer API",
    description="Adan Guerrero Aguilar",
    version="1.0.1")

# Base de datos simulada con objetos modelUsuario
usuarios: List[modelUsuario] = [
    modelUsuario(id=1, nombre="Adan", edad=21, correo="adan@example.com"),
    modelUsuario(id=2, nombre="Jacinto", edad=20, correo="jacinto@example.com"),
    modelUsuario(id=3, nombre="Gabriel", edad=19, correo="gabriel@example.com"),
    modelUsuario(id=4, nombre="Kanicas", edad=33, correo="kanicas@example.com"),
    modelUsuario(id=5, nombre="Elver", edad=13, correo="elver@example.com")
]

@app.get("/", tags=["Inicio"])
def main():
    return {"hello FastAPI": "AdanGuerrero"}

@app.post("/auth", tags=["Autentificacion"])
def login(autorizado:modelAuth):
    if autorizado.correo == 'Adan@example.com' and autorizado.passw == '123456789':
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse (conten= token)
    else:
        return{"Aviso":"Usuario no autorizado"}


# Endpoint para consultar todos los usuarios
@app.get("/usuarios", dependencies=[Depends(BearerJWT())] response_model=List[modelUsuario], tags=["Operaciones CRUD"])
def consultar_todos():
    return usuarios

# Endpoint para agregar un usuario
@app.post("/usuarios/", response_model=modelUsuario, tags=["Operaciones CRUD"])
def agregar_usuario(usuarionuevo: modelUsuario):
    for usr in usuarios:
        if usr.id == usuarionuevo.id:
            raise HTTPException(status_code=400, detail="El ID ya está registrado")

    usuarios.append(usuarionuevo)  # Se agrega correctamente como objeto modelUsuario
    return usuarionuevo

# Endpoint para actualizar un usuario
@app.put("/usuarios/{id}", response_model=modelUsuario, tags=["Operaciones CRUD"])
def actualizar_usuario(id: int, usuario_actualizado: modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr.id == id:
            usuarios[index] = usuario_actualizado  # Sustituimos directamente el objeto
            return usuarios[index]

    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Endpoint para eliminar usuario
@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def eliminar_usuario(id: int):
    for index, usuario in enumerate(usuarios):
        if usuario.id == id:
            usuarios.pop(index)  # Eliminamos usando índice para evitar errores
            return {"mensaje": "Usuario eliminado correctamente"}

    raise HTTPException(status_code=404, detail="Usuario no encontrado")
