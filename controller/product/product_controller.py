from fastapi import APIRouter, Request, Path
from fastapi.params import Depends

from app.security.security import get_current_user
from app.service.product.ProductService import ProductService
from dto.product.request.ProductRequestDTO import ProductRequestDTO
from dto.product.response.ProductResponseDTO import ProductResponseDTO
from infrastructure.erro.error_response import ErrorResponse

product_router = APIRouter(dependencies=[Depends(get_current_user)], prefix="/product", tags=["Product"])

class ProductController:
    product_service = ProductService()

    @staticmethod
    @product_router.get(
        "/all",
        summary="Buscar todos os Produto",
        description="Retorna os dados de todos os Produto.",
        tags=["Product"],
        response_model=list[ProductResponseDTO],
        responses={
            200: {"model": list[ProductResponseDTO], "description": "Produtos encontrados"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Produtos não encontrados"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def get_all_product():
        """
    Rota para busca de todos os Produtos
        """
        return ProductController.product_service.get_all_products()

    @staticmethod
    @product_router.get(
        "/",
        summary="Buscar Produtos por filtros",
        description="Retorna os dados de uma lista de Produto por seus filtros.",
        tags=["Product"],
        response_model=list[ProductResponseDTO],
        responses={
            200: {"model": ProductResponseDTO, "description": "Produto encontrado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Produto não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def get_filtered_products( page:int, page_size: int, id_product:int | None = None, id_stock:int | None = None, unit_value: float | None = None,  id_category:int | None = None,  active:bool | None = None,  name:str | None = None):
        """
    Rota para busca de Produtos por filtros
        """
        return ProductController.product_service.get_filtered_products(page, page_size, id_product, id_stock, unit_value, id_category, active, name)

    @staticmethod
    @product_router.get(
        "/{product_id}",
        summary="Buscar Produto por ID",
        description="Retorna os dados de um Produto pelo seu identificador.",
        tags=["Product"],
        response_model=ProductResponseDTO,
        responses={
            200: {"model": ProductResponseDTO, "description": "Produto encontrado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Produto não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def get_product(product_id: int = Path(..., gt=0)):
        """
    Rota para busca o Produto pelo ID
        """
        return ProductController.product_service.find_by_id(product_id)

    @staticmethod
    @product_router.post(
        "/",
        summary="Criar um produto",
        description="Cria um produto.",
        tags=["Product"],
        response_model=ProductResponseDTO,
        responses={
            200: {"model": ProductResponseDTO, "description": "Produto criado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Categoria não encontrado"},
            409: {"model": ErrorResponse, "description": "Produto ja existente"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def create_product(product_request: ProductRequestDTO):
        """
    Rota para criar um produto
        """
        return ProductController.product_service.create_product(product_request)

    @staticmethod
    @product_router.put(
        "/{product_id}",
        summary="Altera um produto",
        description="Alterar um produto.",
        tags=["Product"],
        response_model=ProductResponseDTO,
        responses={
            200: {"model": ProductResponseDTO, "description": "Produto alterado"},
            400: {"model": ErrorResponse, "description": "requisição invalida"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Produto ou categoria não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def update_product(product_id: int, product_request: ProductRequestDTO):
        """
    Rota para alterar um Produto
        """
        return ProductController.product_service.update_product(product_id,product_request)

    @staticmethod
    @product_router.delete(
        "/{product_id}",
        summary="Deletar um produto",
        description="Deleta um produto.",
        tags=["Product"],
        responses={
            200: {"model": "", "description": "Produto deletado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Produto não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def delete_product(product_id: int):
        """
    Rota para deletar o Produto pelo ID
        """
        return ProductController.product_service.delete_by_id(product_id)

