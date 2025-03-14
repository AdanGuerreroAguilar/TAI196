from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from pydantic import BaseModel, Field

app= FastAPI(
    title='Mi primer API',
    description='Adan Guerrero Aguilar',
    version='1.0.1'

)

class modelEnvios(BaseModel):
    CP:str = Field(..., min_length=5, description="El CP debe contener 5 digitos")
    Destino:str = Field(..., min_length=6, description="El destino debe contener al menos 6 caracteres")
    Peso:int = Field(..., min_length=0, max_length=500, description="El peso debe ser un valor entero entre 0 y 500")

Envios: List[modelEnvios] = [
    modelEnvios(CP="12345", Destino="CDMX", Peso=100),
    modelEnvios(CP="54321", Destino="Qro", Peso=150),
    modelEnvios(CP="76080", Destino="Puebla", Peso=120),
    modelEnvios(CP="01010", Destino="España", Peso=123),
]


@app.get('/',tags=['Inicio'])
def main():
    return{'hello FastAPI':'Bienvenido Administrador'}

#endpoint Consultar todos los envios

@app.get("/envios", response_model=List[modelEnvios], tags=["Operaciones CRUD"])
def consultar_todos():
    return Envios

# Endpoint para eliminar Envio (DELETE)

@app.delete("/envios/{CP}", tags=["Operaciones CRUD"])
def eliminar_envio(CP: int):
    for index, Envios in enumerate(Envios):
        if Envios.CP == CP:
            Envios.pop(index)  # Eliminamos usando índice para evitar errores
            return {"mensaje": "Envio eliminado correctamente"}

    raise HTTPException(status_code=404, detail="Envio no encontrado")


