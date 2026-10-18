from model.stock_product import StockProduct


class StockResponseDTO:
    def __init__(self,stock_id: int, product_id: int, quantity: int):
        self.stock_id = stock_id
        self.product_id = product_id
        self.quantity = quantity

    @staticmethod
    def from_stock(stock: StockProduct):
        return StockResponseDTO(stock.get_id(),stock.get_product_id(),stock.get_quantity())
