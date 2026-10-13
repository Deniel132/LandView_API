from pydantic import EmailStr
from model.enums.user_role import UserRole
from model.user import User


class UserResponseDTO:
    def __init__(self,user_id: int, email: EmailStr, role: UserRole):
        self.user_id = user_id
        self.email = email
        self.role = role

    @staticmethod
    def from_user(user: User):
        return UserResponseDTO(user.get_id(), user.get_email(), user.get_role())