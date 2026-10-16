from fastapi import APIRouter

from app.service.category.CategoryService import CategoryService
from dto.category.request.CategoryRequestDTO import CategoryRequestDTO

category_router = APIRouter(prefix="/category", tags=["Category"])

class CategoryController:
    category_service = CategoryService()

    @staticmethod
    @category_router.get("/{category_id}")
    def get_category(category_id: int):
        """
    Rota para busca o Categoria pelo ID
        """
        return CategoryController.category_service.find_by_id(category_id)

    @staticmethod
    @category_router.post("/")
    def create_category(category_request: CategoryRequestDTO):
        """
    Rota para criar uma categoria
        """

        return CategoryController.category_service.create_category(category_request)

    @staticmethod
    @category_router.put("/{category_id}")
    def update_stock(category_id: int, category_request: CategoryRequestDTO):
        """
    Rota para alterar uma Categoria
        """
        return CategoryController.category_service.update_category(category_id, category_request)

    @staticmethod
    @category_router.delete("/{category_id}")
    def delete_stock(category_id: int):
        """
    Rota para deletar a Categoria pelo ID
        """
        return CategoryController.category_service.delete_category(category_id)

