from fastapi import FastAPI
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

@app.get('/promedio',tags=['Mi Calificacion '])
def promedio():
    return 9

@app.get('/usuario/{id}',tags=['Parametro obligatorio '])
def ConsultaUsuario(id:int):
    #conectamosBD
    #hacemos consulta retornamos resultest
    return{"Se encontro el usuario": id}

@app.get('/usuario/',tags=['Parametro opcional'])
def ConsultaUsuario2(id:Optional[int] = None):
    if id is not None: 
        for usuario in usuarios:
            if usuario["id"]==id:
                return{"mensaje":"Usuario encontrado","usuario":usuario}
        return{"mensaje":f"No se encontro el id: {id}"}
    else:
        return{"mensaje":"No se proporciono un id"}


@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    id: Optional[int] = None,#error en el nombre c:
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (id is None or usuario["id"] == id) and #error en el nombre c:
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}