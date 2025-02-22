from fastapi import FastAPI, HTTPException
from typing import Optional, List
from pydantic import BaseModel

app= FastAPI(
    title='Mi primer API',
    description='Adan Guerrero Aguilar',
    version='1.0.1'

)
#modelo para validacion de datos 
class modelUsuario(BaseModel):
    id: int
    nombre: str
    edad: int
    correo: str 



usuarios=[
    {"id":1,"nombre":"Adan","edad":21, "correo":"adan@example.com"},
    {"id":2,"nombre":"Jacinto","edad":20, "correo":"jacinto@example.com"},
    {"id":3,"nombre":"Gabriel","edad":19, "correo":"gabriel@example.com"},
    {"id":4,"nombre":"kanicas","edad":33, "correo":"kanicas@example.com"},
    {"id":5,"nombre":"Elver","edad":13, "correo":"elver@example.com"}
]


@app.get('/',tags=['Inicio'])
def main():
    return{'hello FastAPI':'AdanGuerrero'}

#endpoint Consultar datos 
@app.get('/usuarios',response_model= List[modelUsuario],tags=['Operaciones CRUD'])
def ConsultarTodos():
    return usuarios

#endpoint Para Agregar usuarios
@app.post('/usuarios/', response_model= modelUsuario, tags=['Operaciones CRUD'])
def AgregarUsuarios(usuarionuevo: modelUsuario):
        for usr in usuarios:
            if usr ["id"] == usuarionuevo.id:
                raise HTTPException(status_code=400, detail="EL ID YA ESTA REGISTRADO")
            
        usuarios.append(usuarionuevo)
        return usuarionuevo
            
# Endpoint para actualizar usuario (PUT)
@app.put('/usuarios/{id}',response_model= modelUsuario, tags=['Operaciones CRUD'])
def actualizar_usuario(id: int, usuario_actualizado:modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr ["id"] == id:
            usuarios[index]= usuario_actualizado.model_dump()
            return usuarios[index]
        
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Endpoint para eliminar usuario (DELETE)
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")