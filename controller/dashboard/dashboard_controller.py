from fastapi import APIRouter
from fastapi.params import Depends

from app.security.security import get_current_user
from app.service.dashboard.DashboardService import DashboardService
from dto.dashboard.DashboardResponseDTO import DashboardResponseDTO
from infrastructure.erro.error_response import ErrorResponse

dashboard_router = APIRouter(dependencies=[Depends(get_current_user)] ,prefix="/dashboard", tags=["Dashboard"])

class DashboardController(APIRouter):
    dashboard_service = DashboardService()

    @staticmethod
    @dashboard_router.get(
        "/",
        summary="Ver Produto com Maior e Menor Estoque",
        description="Retorna o Produto com Maior e Menor Estoque.",
        tags=["Dashboard"],
        response_model=DashboardResponseDTO,
        responses={
            200: {"model": DashboardResponseDTO, "description": "Produto encontrado"},
            401: {"model": ErrorResponse, "description": "Não autorizado"},
            404: {"model": ErrorResponse, "description": "Produto não encontrado"},
            500: {"model": ErrorResponse, "description": "Erro interno"},
        },)

    def get_low_high_stock_dashboard():
        """
    Rota para buscar produtos com maior e menor estoque
        """
        return DashboardController.dashboard_service.get_stock_dashboard()

    @staticmethod
    @dashboard_router.get(
        "/best-selling",
        summary="Ver os 10 produtos mais vendidos",
        description="Retorna os produtos com maior quantidade de vendas.",
        responses={
            200: {"description": "Produtos encontrados"},
            401: {"model": ErrorResponse},
            500: {"model": ErrorResponse},
        }
    )
    def get_best_selling_products():
        """ Retorna os produtos com maior quantidade de vendas"""
        return DashboardController.dashboard_service.get_best_selling_products()