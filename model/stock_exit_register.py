from sqlalchemy import Column, Integer, ForeignKey

from config.data_base.database import Base
from model.product import Product


class StockExitRegister(Base):
    __tablename__ = "stock_exit_register"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)
    __id_product = Column("id_product",Integer,ForeignKey("product.id"),nullable=False)
    __id_user = Column("id_user",Integer,ForeignKey("user.id"),nullable=False)
    __id_stock = Column("id_stock",Integer,ForeignKey("stock_product.id"),nullable=False)
    __quantity = Column("quantity", Integer, nullable=False, default=0)

    def __init__(self, id_product: int, id_user: int, id_stock: int, quantity: int, id: int = None, **kw):
        super().__init__(**kw)
        self.__id = id
        self.__id_product = id_product
        self.__id_user = id_user
        self.__id_stock = id_stock
        self.__quantity = quantity

    @staticmethod
    def from_dict(data: dict) -> "StockExitRegister":
        return StockExitRegister(
            id_product=data["id_product"],
            id_user=data["id_user"],
            id_stock=data["id_stock"],
            quantity=data["quantity"],
            id=data.get("id")
        )
    def to_dict(self) -> dict:
        product_id = self.__id_product

        if isinstance(product_id, Product):
            product_id = product_id.get_id()

        return {
            "id_product": product_id,
            "id_user": self.__id_user,
            "id_stock": self.__id_stock,
            "quantity": self.__quantity
        }

    def get_id(self):
        return self.__id

    def get_product_id(self):
        return self.__id_product

    def set_product(self, product):
        self.__id_product = product.id

    def set_user(self, user):
        self.__id_user = user.id

    def get_user_id(self):
        return self.__id_user

    def set_stock_product(self, stock_product):
        self.__id_stock = stock_product.id

    def get_stock_product_id(self):
        return self.__id_stock

    def get_quantity(self) -> int:
        return self.__quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        self.__quantity = quantity
