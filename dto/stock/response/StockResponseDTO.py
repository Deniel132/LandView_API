from pydantic import BaseModel

from model.stock_product import StockProduct


class StockResponseDTO(BaseModel):
    stock_id: int
    product_id: int
    quantity : int

    @staticmethod
    def from_stock(stock: StockProduct):
        return StockResponseDTO(stock_id=stock.get_id(),product_id=stock.get_product_id(),quantity=stock.get_quantity())
