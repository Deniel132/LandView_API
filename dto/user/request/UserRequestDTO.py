from pydantic import EmailStr,BaseModel


class UserRequestDTO(BaseModel):
    email: EmailStr
    password: str
    role: str