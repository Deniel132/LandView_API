from pydantic import EmailStr,BaseModel

class UserLoginDTO(BaseModel):
    email: EmailStr
    password: str