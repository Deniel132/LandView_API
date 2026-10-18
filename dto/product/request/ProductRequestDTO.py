from pydantic import BaseModel


class ProductRequestDTO(BaseModel):
    product_name: str
    unit_value: float
    product_category_id: int