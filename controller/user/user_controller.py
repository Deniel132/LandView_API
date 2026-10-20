from fastapi import APIRouter, Depends

from app.security.security import get_current_user
from app.service.user.UserService import UserService
from config.routes.user.user_routes import UserRoutes
from dto.user.request.UserLoginDTO import UserLoginDTO
from dto.user.request.UserRequestDTO import UserRequestDTO
from model.user import User

user_router = APIRouter(dependencies=[Depends(get_current_user)], prefix=UserRoutes.USER_PREFIX, tags=["Usuarios"])
user_public_router = APIRouter(prefix=UserRoutes.USER_PREFIX, tags=["Usuarios"])

class UserController:
    service = UserService()

    @staticmethod
    @user_router.get("/private")
    def private_route(current_user: User = Depends(get_current_user) ):
        return {
            "message": "Autenticado com sucesso",
            "email": current_user.get_email(),
            "role": current_user.get_role()
        }


    @staticmethod
    @user_public_router.post("/login")
    def __login(request : UserLoginDTO):
        return UserController.service.login(request)

    @staticmethod
    @user_router.get("/{user_id}")
    def __get_user_by_id(user_id: int):
        """
        Rota para busca de usuarios pelo seu id
        """
        return UserController.service.find_by_id(user_id)

    @staticmethod
    @user_public_router.post("/")
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




