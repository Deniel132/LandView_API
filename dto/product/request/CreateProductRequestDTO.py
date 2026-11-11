from pydantic import BaseModel, Field
from sqlalchemy import null

from dto.stock.request.CreateStockRequestDTO import CreateStockRequestDTO


class CreateProductRequestDTO(BaseModel):
    category_id: int
    product_name: str
    unit_value: float
    stock_item_dto: list[CreateStockRequestDTO]
    images: list[str] | None = None