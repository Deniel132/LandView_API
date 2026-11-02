from pydantic import BaseModel


class CreateStockRequestDTO(BaseModel):
    characteristics: str
    sub_characteristics: str
    quantity: int