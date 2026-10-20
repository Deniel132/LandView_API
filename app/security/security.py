from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from model.user import User
from repository.user.UserRepository import UserRepository

security = HTTPBearer(auto_error=False)



def get_current_user(credentials: HTTPAuthorizationCredentials | None = Depends(security))-> User:
    if credentials is None:
        raise HTTPException(status_code=401, detail="Autenticaçâo do token não informado", headers={"WWW-Authenticate": "Bearer"})

    token = credentials.credentials
    user = UserRepository.find_by_token(token)

    if user is None:
        raise HTTPException(status_code=401, detail="Token invalido", headers={"WWW-Authenticate": "Bearer"})

    if not user.get_active():
        raise HTTPException(status_code=401, detail="Usuario inativo" , headers={"WWW-Authenticate": "Bearer"})

    return user
