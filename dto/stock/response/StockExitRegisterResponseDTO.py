from pydantic import BaseModel
from model.stock_exit_register import StockExitRegister

class StockExitRegisterResponseDTO(BaseModel):
    id: int
    id_product: int
    id_user: int
    id_stock: int
    quantity: int


    @staticmethod
    def from_model(register: StockExitRegister) -> 'StockExitRegisterResponseDTO':
        return StockExitRegisterResponseDTO(
            id=register.get_id(),
            id_product=register.get_product_id(),
            id_user=register.get_user_id(),
            id_stock=register.get_stock_product_id(),
            quantity=register.get_quantity(),
        )