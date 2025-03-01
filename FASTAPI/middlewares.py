from fastapi import HTTPException, request
from fastapi.security import HTTPBearer
from tokenGen import validateToken

class BearerJWT(HTTPBearer):
    async def __call__(self, request:request):
        auth= await super().__call__(request)
        data= validateToken(auth.credentials)

        if not isinstance(data,dict):
            raise HTTPException(status_code=401, detail= 'El formato del token no es valido ')
        
        if data.get('correo')!= 'adan@example.com':
            raise HTTPException(status_code=403, detail= 'Credenciales no validas')
        