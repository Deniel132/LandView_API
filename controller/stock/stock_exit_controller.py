from fastapi import APIRouter
from fastapi.params import Depends

from app.security.security import get_current_user
from app.service.stock.StockService import StockService
from app.service.stock.StoqueExitService import StockExitService
from dto.stock.request.StoqueExitRequestDTO import StockExitRequestDTO
from dto.stock.response.StockResponseDTO import StockResponseDTO
from infrastructure.erro.error_response import ErrorResponse
from dto.stock.response.StockExitRegisterResponseDTO import StockExitRegisterResponseDTO
from model.user import User

stock_exit_router = APIRouter(dependencies=[Depends(get_current_user)] ,prefix="/stock-exit", tags=["Stock-exit"])

class StockExitController:
    stock_service = StockService()
    stock_exit_service = StockExitService()

    def __init__(self):
        pass

    @staticmethod
    @stock_exit_router.post(
        "/",
        summary="Registrar saida de estoque",
        description="Registra uma saida de estoque.",
        tags=["Stock-exit"],
        response_model=StockResponseDTO,
        responses={
            200: {"model": StockResponseDTO, "description": "Saida registrada"},
            400: {"model": ErrorResponse, "description": "requisição invalida"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Estoque não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def do_exit_stock(exit_request: StockExitRequestDTO, current_user:User = Depends(get_current_user)):
        """
    Rota para registrar saidas de estoque
        """
        return StockExitController.stock_exit_service.do_exit(exit_request, current_user)

    @staticmethod
    @stock_exit_router.get(
        "/",
        summary="Retorna o historico de saidas de estoque",
        description="Retorna o historico de saidas de estoque.",
        tags=["Stock-exit"],
        response_model=list[StockExitRegisterResponseDTO],
        responses={
            200: {"model": list[StockExitRegisterResponseDTO], "description": "historico encontrado"},
            400: {"model": ErrorResponse, "description": "requisição invalida"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },
    )
    def do_exit_stock(page:int, page_size: int, id_product:int | None = None, id_stock:int | None = None, id_user:int | None = None ):
        """
    Rota para registrar saidas de estoque
        """
        return StockExitController.stock_exit_service.get_pageable_history(
            page,
            page_size,
            id_product,
            id_stock,
            id_user
        )