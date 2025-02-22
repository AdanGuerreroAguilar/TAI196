from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title='API de Tareas',
    description='Gestión de tareas con FastAPI',
    version='1.0.0'
)

tareas = [{"id":1,"nombre":"tarea2"},
          {"id":2,"nombre":"tarea1"},
          {"id":3,"nombre":"tarea3"}
          ]
contador_id = 1

@app.get('/', tags=['Inicio'])
def main():
    return {'hello FastAPI': 'Gestión de Tareas'}

# Obtener todas las tareas
@app.get('/tareas', tags=['Operaciones CRUD'])
def obtener_tareas():
    return {"Tareas Registradas": tareas}

# Obtener una tarea por ID
@app.get('/tareas/{id}', tags=['Operaciones CRUD'])
def obtener_tarea(id: int):
    tarea = next((t for t in tareas if t['id'] == id), None)
    if tarea:
        return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Crear una nueva tarea
@app.post('/tareas/', tags=['Operaciones CRUD'])
def crear_tarea(nueva_tarea: dict):
    global contador_id
    for tarea in tareas:
        if tarea["id"] == nueva_tarea.get("id"):
            raise HTTPException(status_code=400, detail="EL ID YA ESTÁ REGISTRADO")
    
    nueva_tarea["id"] = contador_id
    tareas.append(nueva_tarea)
    contador_id += 1
    return nueva_tarea

# Actualizar una tarea existente
@app.put('/tareas/{id}', tags=['Operaciones CRUD'])
def actualizar_tarea(id: int, tarea_actualizada: dict):
    for tarea in tareas:
        if tarea["id"] == id:
            tarea.update(tarea_actualizada)
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# Eliminar una tarea
@app.delete('/tareas/{id}', tags=['Operaciones CRUD'])
def eliminar_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            tareas.remove(tarea)
            return {"mensaje": "Tarea eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")