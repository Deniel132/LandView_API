from fastapi import APIRouter
from fastapi.params import Depends

from app.security.security import get_current_user
from app.service.category.CategoryService import CategoryService
from dto.category.request.CategoryRequestDTO import CategoryRequestDTO
from dto.category.response.CategoryResponseDTO import CategoryResponseDTO
from infrastructure.erro.error_response import ErrorResponse

category_router = APIRouter(dependencies=[Depends(get_current_user)] ,prefix="/category", tags=["Category"])

class CategoryController:
    category_service = CategoryService()

    @staticmethod
    @category_router.get(
        "/{category_id}",
        summary="Buscar Categoria por ID",
        description="Retorna os dados de um Categoria pelo seu identificador.",
        tags=["Category"],
        response_model=CategoryResponseDTO,
        responses={
            200: {"model": CategoryResponseDTO, "description": "Categoria encontrado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Categoria não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def get_category(category_id: int):
        """
    Rota para busca o Categoria pelo ID
        """
        return CategoryController.category_service.find_by_id(category_id)

    @staticmethod
    @category_router.post(
        "/",
        summary="Criar Categoria",
        description="Cria uma Categoria.",
        tags=["Category"],
        response_model=CategoryResponseDTO,
        responses={
            200: {"model": CategoryResponseDTO, "description": "Categoria criada"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def create_category(category_request: CategoryRequestDTO):
        """
    Rota para criar uma categoria
        """

        return CategoryController.category_service.create_category(category_request)

    @staticmethod
    @category_router.put(
        "/{category_id}",
        summary="Altera Categoria",
        description="Altera uma Categoria.",
        tags=["Category"],
        response_model=CategoryResponseDTO,
        responses={
            200: {"model": CategoryResponseDTO, "description": "Categoria alterada"},
            400: {"model": ErrorResponse, "description": "requisição invalida"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def update_category(category_id: int, category_request: CategoryRequestDTO):
        """
    Rota para alterar uma Categoria
        """
        return CategoryController.category_service.update_category(category_id, category_request)

    @staticmethod
    @category_router.delete(
        "/{category_id}",
        summary="Deleta Categoria por ID",
        description="Delta uma Categoria.",
        tags=["Category"],
        responses={
            200: {"model": "", "description": "Categoria deletada"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def delete_category(category_id: int):
        """
    Rota para deletar a Categoria pelo ID
        """
        return CategoryController.category_service.delete_category(category_id)

