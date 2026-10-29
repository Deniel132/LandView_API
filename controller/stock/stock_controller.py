from fastapi import APIRouter
from fastapi.params import Depends

from app.security.security import get_current_user
from app.service.stock.StockService import StockService
from dto.stock.request.StockRequestDTO import StockRequestDTO
from dto.stock.response.StockResponseDTO import StockResponseDTO
from infrastructure.erro.error_response import ErrorResponse

stock_router = APIRouter(dependencies=[Depends(get_current_user)] ,prefix="/stock", tags=["Stock"])

class StockController:
    stock_service = StockService()

    def __init__(self):
        pass

    @staticmethod
    @stock_router.get(
        "/{stock_id}",
        summary="Buscar Estoque por ID",
        description="Retorna os dados de um Estoque pelo seu identificador.",
        tags=["Stock"],
        response_model=StockResponseDTO,
        responses={
            200: {"model": StockResponseDTO, "description": "Estoque encontrado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Estoque não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def get_stock(stock_id: int):
        """
    Rota para busca do Estoque pelo ID
        """
        return StockController.stock_service.find_by_id(stock_id)

    @staticmethod
    @stock_router.post(
        "/",
        summary="Fazer uma movimentacao de stock",
        description="faz uma movimentacao de stock.",
        tags=["Stock"],
        response_model=StockResponseDTO,
        responses={
            200: {"model": StockResponseDTO, "description": "Estoque criado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Produto não encontrado"},
            409: {"model": ErrorResponse, "description": "stock ja existente"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def create_stock(stock_request: StockRequestDTO):
        """
    Rota para fazer uma movimentacao de stock
        """

        return StockController.stock_service.create(stock_request)

    @staticmethod
    @stock_router.put(
        "/{stock_id}",
        summary="Fazer uma alteraração de stock",
        description="faz uma alteraração de stock.",
        tags=["Stock"],
        response_model=StockResponseDTO,
        responses={
            200: {"model": StockResponseDTO, "description": "Estoque alterado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def update_stock(stock_id: int, stock_request: StockRequestDTO):
        """
    Rota para alterar um Estoque
        """
        return StockController.stock_service.update(stock_id, stock_request)


    @staticmethod
    @stock_router.delete(
        "/{stock_id}",
        summary="Deleta uma stock",
        description="deletar stock.",
        tags=["Stock"],
        responses={
            200: {"model": "", "description": "Estoque deletado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "stock não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def delete_stock(stock_id: int):
        """
    Rota para deletar o Estoque pelo ID
        """
        return StockController.stock_service.delete(stock_id)

