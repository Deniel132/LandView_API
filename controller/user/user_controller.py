import numbers
from fastapi import APIRouter

from app.service.user.UserService import UserService
from config.routes.user.user_routes import UserRoutes
from dto.user.request.UserRequestDTO import UserRequestDTO
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

    @staticmethod
    @user_router.post("/")
    def __crate_user(user_request_dto: UserRequestDTO):
        """
        Rota para criar usuarios
        """
        return UserController.service.create_user(user_request_dto)

    @staticmethod
    @user_router.put("/{user_id}")
    def __update_user(user_id: int, user_request_dto: UserRequestDTO):
        """
        Rota para atualizar usuarios
        """
        return UserController.service.update_user(user_id, user_request_dto)


    @staticmethod
    @user_router.delete("/{user_id}")
    def __delete_user_by_id(user_id: int):
        """
        Rota para deletar usuarios
        """
        return UserController.service.delete_by_id(user_id)




