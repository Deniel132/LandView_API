from pydantic import BaseModel


class StockRequestDTO(BaseModel):
    product_id: int
    characteristics: str
    sub_characteristics: str
    quantity: int