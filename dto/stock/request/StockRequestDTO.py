from pydantic import BaseModel


class StockRequestDTO(BaseModel):
    product_id: int
    quantity: int