from pydantic import EmailStr,BaseModel
from model.enums.user_role import UserRole


class UserRequestDTO(BaseModel):
    email: EmailStr
    password: str
    role: UserRole