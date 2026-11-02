from fastapi import APIRouter, Depends

from app.security.security import get_current_user
from app.service.user.UserService import UserService
from config.routes.user.user_routes import UserRoutes
from dto.user.request.UserRequestDTO import UserRequestDTO
from dto.user.request.UserLoginDTO import UserLoginDTO
from dto.user.response.UserResponseDTO import UserResponseDTO
from infrastructure.erro.error_response import ErrorResponse

user_router = APIRouter(dependencies=[Depends(get_current_user)], prefix=UserRoutes.USER_PREFIX, tags=["Usuarios"])
user_public_router = APIRouter(prefix=UserRoutes.USER_PREFIX, tags=["Usuarios"])

class UserController:
    service = UserService()

    @staticmethod
    @user_public_router.post(
        "/login",
        summary="Logar na API",
        description="Retorna o token de um usuário ao se autenticar.",
        tags=["Usuarios"],
        response_model=str,
        responses={
            200: {"model": str, "description": "Usuário logado"},
            400: {"model": ErrorResponse, "description": "requisição invalida"},
            404: {"model": ErrorResponse, "description": "Usuário não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def __login(request: UserLoginDTO):
        return UserController.service.login(request)

    @staticmethod
    @user_router.get(
        "/{user_id}",
        summary="Buscar usuário por ID",
        description="Retorna os dados de um usuário pelo seu identificador.",
        tags=["Usuarios"],
        response_model=UserResponseDTO,
        responses={
            200: { "model": UserResponseDTO, "description": "Usuário encontrado"},
            401: { "model": ErrorResponse, "description": "Não autorizado"},
            404: { "model": ErrorResponse, "description": "Usuário não encontrado"},
            500: { "model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def __get_user_by_id(user_id: int):
        """
        Rota para busca de usuarios pelo seu id
        """
        return UserController.service.find_by_id(user_id)

    @staticmethod
    @user_public_router.post(
        "/",
        summary="Criar usuários",
        description="Cria um usuário na API",
        tags=["Usuarios"],
        response_model=UserResponseDTO,
        responses={
            200: {"model": UserResponseDTO, "description": "Usuário cadastrado"},
            400: {"model": ErrorResponse, "description": "requisição invalida"},
            409: {"model": ErrorResponse, "description": "Usuário ja existente"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def __crate_user(user_request_dto: UserRequestDTO):
        """
        Rota para criar usuarios
        """
        return UserController.service.create_user(user_request_dto)

    @staticmethod
    @user_router.put(
        "/{user_id}",
        summary="Atualizar usuarios",
        description="Atualiza as informações de um usuário pelo seu identificador.",
        tags=["Usuarios"],
        response_model=UserResponseDTO,
        responses={
            200: {"model": UserResponseDTO, "description": "Usuário atualizado"},
            400: {"model": ErrorResponse, "description": "requisição invalida"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Usuário não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def __update_user(user_id: int, user_request_dto: UserRequestDTO):
        """
        Rota para atualizar usuarios
        """
        return UserController.service.update_user(user_id, user_request_dto)


    @staticmethod
    @user_router.delete(
        "/{user_id}",
        summary=" Deletar usuarios por ID",
        description="Deleta um usuário pelo seu identificador.",
        tags=["Usuarios"],
        responses={
            200: {"model": "", "description": "Usuário deletado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Usuário não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def __delete_user_by_id(user_id: int):
        """
        Rota para deletar usuarios
        """
        return UserController.service.delete_by_id(user_id)




