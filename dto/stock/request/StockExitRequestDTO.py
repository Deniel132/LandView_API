from pydantic import BaseModel


class StockExitRequestDTO(BaseModel):
    stock_id: int
    quantity: int