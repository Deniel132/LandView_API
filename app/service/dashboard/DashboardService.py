from dto.dashboard.ProductDashboardDTO import ProductDashboardDTO
from dto.dashboard.DashboardResponseDTO import DashboardResponseDTO
from dto.dashboard.StockDashboardDTO import StockDashboardDTO
from repository.product.ProductRepository import ProductRepository
from repository.stock.StockRepository import StockRepository


class DashboardService:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.stock_repository = StockRepository()

    def get_stock_dashboard(self):
            lowest = self.stock_repository.find_product_with_lowest_stock()
            highest = self.stock_repository.find_product_with_highest_stock()

            lowest_dto = None
            highest_dto = None

            if lowest:
                product = self.product_repository.find_by_id(lowest.get_product_id())

                lowest_dto = StockDashboardDTO(product_id=lowest.get_product_id(), product_name=product.get_product_name(),unit_value=product.get_unit_value(),quantity=lowest.get_quantity())

            if highest:
                product = self.product_repository.find_by_id(highest.get_product_id())

                highest_dto = StockDashboardDTO(product_id=highest.get_product_id(), product_name=product.get_product_name(),unit_value=product.get_unit_value(), quantity=highest.get_quantity())

            return DashboardResponseDTO(lowest_stock=lowest_dto, highest_stock=highest_dto
            )

    def get_best_selling_products(self):
        products = self.product_repository.get_best_selling_products()

        return [
            ProductDashboardDTO(**product)
            for product in products
        ]