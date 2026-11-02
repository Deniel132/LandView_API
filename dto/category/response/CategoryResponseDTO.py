from pydantic import BaseModel

from model.product_category import ProductCategory


class CategoryResponseDTO(BaseModel):
    category_id: int
    category_name: str
    category_type: str



    @staticmethod
    def from_category(category:ProductCategory):
        return CategoryResponseDTO(category_id=category.get_id(), category_name=category.get_category_name(), category_type=category.get_category_type())