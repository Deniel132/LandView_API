
from fastapi import APIRouter, Path, Body, Query
from fastapi.params import Depends

from app.security.security import get_current_user
from app.service.img.ImageService import ImageService
from infrastructure.erro.error_response import ErrorResponse
from dto.img.request.ImageRequestDTO import ImageRequestDTO

image_router = APIRouter(
    dependencies=[Depends(get_current_user)],
    prefix="/images",
    tags=["Images"]
)


class ImageController:
    image_service = ImageService()

    @staticmethod
    @image_router.post(
        "/product/{product_id}",
        summary="Cadastrar imagens de um produto",
        description="Cadastra uma ou várias imagens vinculadas a um produto.",
        responses={
            200: {"description": "Imagens cadastradas"},
            400: {"model": ErrorResponse, "description": "Imagem inválida"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Produto não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def create_images(
        product_id: int = Path(..., gt=0),
        request: ImageRequestDTO = Body(...)
    ):
        return ImageController.image_service.create_files(
            product_id,
            request.images
        )

    @staticmethod
    @image_router.delete(
        "/product/{product_id}/{image_id}",
        summary="Deletar imagem",
        description="Remove uma imagem do Storage e seu registro no banco.",
        responses={
            200: {"description": "Imagem deletada"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Imagem não encontrada"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def delete_image(
        product_id: int = Path(..., gt=0),
        image_id: int = Path(..., gt=0)
    ):
        return ImageController.image_service.delete_file(
            product_id,
            image_id
        )

    @staticmethod
    @image_router.get(
        "/product/{product_id}",
        summary="Buscar imagens de um produto",
        description="Retorna todas as imagens vinculadas a um produto.",
        responses={
            200: {"description": "Imagens encontradas"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def get_images(
            product_id: int = Path(..., gt=0)
    ):
        return ImageController.image_service.get_all_images_by_product(
            product_id
        )

    @staticmethod
    @image_router.get(
        "/product/{product_id}/all",
        summary="Buscar todas as imagens de um produto",
        description="Retorna todas as imagens vinculadas ao produto.",
        responses={
            200: {"description": "Imagens encontradas"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def get_all_images(
            product_id: int = Path(..., gt=0)
    ):
        return ImageController.image_service.get_all_images_by_product(
            product_id
        )

    @staticmethod
    @image_router.get(
        "/product/{product_id}",
        summary="Buscar imagens de um produto",
        description="Retorna as imagens de um produto, permitindo filtros.",
        responses={
            200: {"description": "Imagens encontradas"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def get_images(
        product_id: int = Path(..., gt=0),
        image_id: int | None = Query(default=None, gt=0),
        image_name: str | None = Query(default=None, min_length=1)
    ):
        return ImageController.image_service.get_images_by_filters(
            product_id,
            image_id,
            image_name
        )

