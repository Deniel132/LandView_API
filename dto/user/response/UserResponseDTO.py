from pydantic import EmailStr, BaseModel
from model.enums.user_role import UserRole
from model.user import User


class UserResponseDTO(BaseModel):
    user_id: int
    email: EmailStr
    role: UserRole

    @staticmethod
    def from_user(user: User):
        return UserResponseDTO(user_id = user.get_id(), email = user.get_email(), role = user.get_role())