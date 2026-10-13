import numbers
from fastapi import APIRouter

from app.service.user.UserService import UserService
from config.routes.user.user_routes import UserRoutes
from model.user import User

user_router = APIRouter(prefix=UserRoutes.USER_PREFIX, tags=["Usuarios"])

class UserController:
    service = UserService()

    @staticmethod
    @user_router.get("/{user_id}")
    def __get_user_by_id(user_id: int):
        """
        Rota para busca de usuarios pelo seu id
        """
        return UserController.service.find_by_id(user_id)


