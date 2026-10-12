from pydantic import BaseModel,Field, EmailStr
from model.enums.user_role import UserRole

class UserResponseDTO:
    user_id: int
    email: EmailStr
    role: UserRole