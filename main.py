from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title='Mi primer API',
    description='Adan Guerrero Aguilar',
    version='1.0.1'

)

usuarios=[
    {"id":1,"nombre":"Adan","edad":21},
    {"id":2,"nombre":"Jacinto","edad":20},
    {"id":3,"nombre":"Gabriel","edad":19},
    {"id":4,"nombre":"kanicas","edad":33},
    {"id":5,"nombre":"Elver","edad":13}
]


@app.get('/',tags=['Inicio'])
def main():
    return{'hello FastAPI':'AdanGuerrero'}

#endpoint Consultar datos 
@app.get('/usuarios',tags=['Operaciones CRUD'])
def ConsultarTodos():
    return{"Usuarios Registrados": usuarios}

#endpoint Para Agregar usuarios
@app.post('/usuarios/',tags=['Operaciones CRUD'])
def AgregarUsuarios(usuarionuevo: dict):
        for usr in usuarios:
            if usr ["id"] == usuarionuevo.get("id"):
                raise HTTPException(status_code=400, detail="EL ID YA ESTA REGISTRADO")
            
        usuarios.append(usuarionuevo)
        return usuarionuevo
            
# Endpoint para actualizar usuario (PUT)
@app.put('/usuarios/{id}', tags=['Operaciones CRUD'])
def actualizar_usuario(id: int, usuario_actualizado: dict):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario.update(usuario_actualizado)
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# Endpoint para eliminar usuario (DELETE)
@app.delete('/usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar_usuario(id: int):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")