from dto.stock.request.StockRequestDTO import StockRequestDTO
from dto.stock.response.StockResponseDTO import StockResponseDTO
from model.stock_product import StockProduct
from repository.stock.StockRepository import StockRepository
from repository.product.ProductRepository import ProductRepository


class StockService:
    def __init__(self):
        self.repository = StockRepository()


    def find_by_id(self, stock_id: int):
        stock = self.repository.find_by_id(stock_id)
        return StockResponseDTO.from_stock(stock)

    def create(self, request: StockRequestDTO):
        product = ProductRepository.find_by_id(request.product_id)

        if product is None:
            raise ValueError("Produto não encontrado")

        stock_product = StockProduct(product, request.quantity)

        saved_stock = self.repository.save_stock_product(stock_product)

        if saved_stock is None:
            return None

        return StockResponseDTO.from_stock(saved_stock)

    def update(self,stock_product_id: int, request: StockRequestDTO):
        stock = self.repository.find_by_id(stock_product_id)
        if stock is None:
            raise ValueError("Estoque não encontrado")

        stock.set_quantity(request.quantity)

        update_stock = self.repository.update_stock_product(stock_product_id,stock)

        return StockResponseDTO.from_stock(update_stock)

    def delete(self,stock_product_id: int):
        delete_stock = self.delete(stock_product_id)
        if delete_stock is None:
            raise ValueError("Estoque não encontrado")

        return "Estoque Deletado com sucesso"