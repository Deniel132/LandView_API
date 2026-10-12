import numbers
from fastapi import APIRouter

from app.service.user.UserService import UserService
from config.routes.user.user_routes import UserRoutes
from model.user import User

user_router = APIRouter(prefix=UserRoutes.USER_PREFIX, tags=["Usuarios"])

class UserController:
    def __init__(self, service: UserService):
        self.service = service


    @user_router.get("/{user_id}")
    def __get_user_by_id(self, user_id: int):
        """
        Rota para busca de usuarios pelo seu id
        """
        return self.service.get_by_id(user_id)


