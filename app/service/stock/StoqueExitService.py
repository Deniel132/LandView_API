from dto.stock.request.StoqueExitRequestDTO import StockExitRequestDTO
from dto.stock.response.StockResponseDTO import StockResponseDTO
from model.user import User
from repository.stock.StockExitRegisterRepository import StockExitRegisterRepository
from repository.stock.StockRepository import StockRepository
from model.stock_exit_register import StockExitRegister

from infrastructure.erro.exceptions.not_found_exception import NotFoundException
from infrastructure.erro.exceptions.bad_request_exception import BadRequestException


class StockExitService:
    def __init__(self):
        self.repository = StockRepository()
        self.exit_register_repository = StockExitRegisterRepository()


    def do_exit(self, exit_request: StockExitRequestDTO, current_user: User):
        stock = self.repository.find_by_id(exit_request.stock_id)

        if not stock:
            raise NotFoundException("Estoque não encontrado")

        if stock.quantity < exit_request.quantity:
            raise BadRequestException("Quantidade para saida informada superior ao registrado no estoque")


        stock.set_quantity(exit_request.quantity)
        exit_register: StockExitRegister = StockExitRegister(stock.get_product().get_id(), current_user.get_id(), exit_request.stock_id, stock.get_quantity())
        self.exit_register_repository.save_register(exit_register)

        return StockResponseDTO.from_stock(stock)