from model.product import Product


class ProductResponseDTO:
    def __init__(self, product_id: int, product_name: str, unit_value: float, product_active: bool):
        self.product_id = product_id
        self.product_name = product_name
        self.unit_value = unit_value
        self.product_active = product_active

    @staticmethod
    def from_product(product: Product):
        return ProductResponseDTO(product.get_id(),product.get_product_name(),product.get_unit_value(),product.get_active())
