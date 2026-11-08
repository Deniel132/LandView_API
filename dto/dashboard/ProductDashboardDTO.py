from pydantic import BaseModel


class ProductDashboardDTO(BaseModel):
    id: int
    product_name: str
    unit_value: float
    total_sold: int
    total_value: float