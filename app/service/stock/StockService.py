from dto.stock.request.StockRequestDTO import StockRequestDTO
from dto.stock.response.StockResponseDTO import StockResponseDTO
from model.stock_product import StockProduct
from repository.stock.StockRepository import StockRepository
from repository.product.ProductRepository import ProductRepository


class StockService:
    def __init__(self):
        self.repository = StockRepository()
        self.product_repository = ProductRepository()

    def __get_by_id(self, stock_product_id: int) -> StockProduct:
        return self.repository.find_by_id(stock_product_id)

    def find_by_id(self, stock_id: int) -> StockResponseDTO:
        stock = self.__get_by_id(stock_id)
        return StockResponseDTO.from_stock(stock)

    def create(self, request: StockRequestDTO):
        product = self.product_repository.find_by_id(request.product_id)

        if product is None:
            raise ValueError("Produto não encontrado")

        existing_stock = self.repository.find_by_product_id(
            request.product_id
        )

        if existing_stock is not None:
            raise ValueError("Este produto já possui um registro de estoque")

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
        delete_stock = self.repository.delete_by_id(stock_product_id)
        if delete_stock is None:
            raise ValueError("Estoque não encontrado")

        return "Estoque Deletado com sucesso"