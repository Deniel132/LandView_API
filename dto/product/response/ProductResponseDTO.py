from pydantic import BaseModel

from model.product import Product


class ProductResponseDTO(BaseModel):
    product_id: int
    product_name: str
    unit_value: float
    product_active: bool

    @staticmethod
    def from_product(product: Product):
        return ProductResponseDTO(product_id=product.get_id(),product_name=product.get_product_name(),unit_value=product.get_unit_value(),product_active=product.get_active())
