from fastapi import APIRouter, Request
from fastapi.params import Depends

from app.security.security import get_current_user
from app.service.product.ProductService import ProductService
from dto.product.request.ProductRequestDTO import ProductRequestDTO

product_router = APIRouter(dependencies=[Depends(get_current_user)], prefix="/product", tags=["Product"])

class ProductController:
    product_service = ProductService()

    @staticmethod
    @product_router.get("/{product_id}")
    def get_product(product_id: int):
        """
    Rota para busca o Produto pelo ID
        """
        return ProductController.product_service.find_by_id(product_id)

    @staticmethod
    @product_router.post("/")
    def create_product(product_request: ProductRequestDTO,request:Request):
        """
    Rota para criar um produto
        """
        protect = get_current_user(request)
        return ProductController.product_service.create_product(product_request)

    @staticmethod
    @product_router.put("/{product_id}")
    def update_product(product_id: int, product_request: ProductRequestDTO):
        """
    Rota para alterar um Produto
        """
        return ProductController.product_service.update_product(product_id,product_request)

    @staticmethod
    @product_router.delete("/{product_id}")
    def delete_product(product_id: int):
        """
    Rota para deletar o Produto pelo ID
        """
        return ProductController.product_service.delete_by_id(product_id)

