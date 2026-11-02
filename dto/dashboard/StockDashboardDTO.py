from pydantic import BaseModel


class StockDashboardDTO(BaseModel):
    product_id: int
    product_name: str
    unit_value: float
    quantity: int