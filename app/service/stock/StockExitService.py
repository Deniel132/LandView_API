from dto.stock.request.StockExitRequestDTO import StockExitRequestDTO
from dto.stock.response.StockExitRegisterResponseDTO import StockExitRegisterResponseDTO
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

        if stock.get_quantity() < exit_request.quantity:
            raise BadRequestException("Quantidade para saida informada superior ao registrado no estoque")

        stock.set_quantity(exit_request.quantity)
        exit_register: StockExitRegister = StockExitRegister(stock.get_product_id(), current_user.get_id(), exit_request.stock_id, stock.get_quantity())
        self.exit_register_repository.save_register(exit_register)
        stock = self.repository.update_stock_product(stock.get_id(), stock)

        return StockResponseDTO.from_stock(stock)


    def get_pageable_history(self, page:int = 1, page_size: int = 10,  id_product:int | None = None, id_stock:int | None = None, id_user:int | None = None ):
        if page < 1 or page_size < 1:
            raise BadRequestException("Pagina ou tamanho de pagina incorreto")

        response =  self.exit_register_repository.get_paged(page, page_size, id_product, id_stock, id_user)
        if not response:
            return []

        history_list = []
        for resp in response:
            history_list.append(StockExitRegisterResponseDTO.from_model(resp))

        return history_list
