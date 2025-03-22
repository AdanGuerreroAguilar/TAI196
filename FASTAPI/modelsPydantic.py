from pydantic import BaseModel, Field, EmailStr

#modelo para validación de datos
class modelUsuario(BaseModel):
    name:str = Field(..., min_length=3, max_length=15, description="Nombre debe contener sólo letras y espacios")
    ege:int = Field(..., gt=0, le=130, description="La edad debe ser mayor a 0 y menor a 130")
    email:str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$', description="Correo válido", example="usuario@example.com")

class modelAuth(BaseModel):    
    correo: EmailStr 
    passw:str =Field(..., min_length=8,strip_whitespace=True, description="Contraseña minimo 8 caracteres")

