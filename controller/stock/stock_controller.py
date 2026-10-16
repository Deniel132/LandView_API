from fastapi import APIRouter
from fastapi.params import Depends

from app.security.security import get_current_user
from app.service.stock.StockService import StockService
from dto.stock.request.StockRequestDTO import StockRequestDTO

stock_router = APIRouter(dependencies=[Depends(get_current_user)] ,prefix="/stock", tags=["Stock"])

class StockController:
    stock_service = StockService()

    def __init__(self):
        pass


    @staticmethod
    @stock_router.get("/{stock_id}")
    def get_stock(stock_id: int):
        """
    Rota para busca do Estoque pelo ID
        """
        return StockController.stock_service.find_by_id(stock_id)

    @staticmethod
    @stock_router.post("/")
    def create_stock(stock_request: StockRequestDTO):
        """
    Rota para fazer uma movimentacao de stock
        """

        return StockController.stock_service.create(stock_request)

    @staticmethod
    @stock_router.put("/{stock_id}")
    def update_stock(stock_id: int, stock_request: StockRequestDTO):
        """
    Rota para alterar um Estoque
        """
        return StockController.stock_service.update(stock_id, stock_request)


    @staticmethod
    @stock_router.delete("/{stock_id}")
    def delete_stock(stock_id: int):
        """
    Rota para deletar o Estoque pelo ID
        """
        return StockController.stock_service.delete(stock_id)

