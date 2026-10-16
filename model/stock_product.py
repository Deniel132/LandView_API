from typing import Any

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from config.data_base.database import Base


class StockProduct(Base):
    __tablename__ = "stock_product"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)
    __id_product = Column("id_product",Integer,ForeignKey("product.id"),nullable=False,unique=True)
    __quantity = Column("quantity", Integer, nullable=False, default=0)
    __product = relationship("Product", back_populates="_Product__stock_item")

    def __init__(self,product,quantity: int,**kw: Any):
        super().__init__(**kw)
        self.__product = product
        self.__quantity = quantity

    @staticmethod
    def from_dict(data: dict) -> "StockProduct":
        stock_product = StockProduct.__new__(StockProduct)
        stock_product._StockProduct__id = data.get("id")
        stock_product._StockProduct__id_product = data.get("id_product")
        stock_product._StockProduct__quantity = data.get("quantity", 0)
        return stock_product

    def to_dict(self) -> dict:
        return {
            "id_product": self.get_id_product(),
            "quantity": self.get_quantity()
        }

    def get_id(self):
        return self.__id

    def get_product_id(self):
        return self.__id_product

    def set_product_id(self, product):
        self.__product = product

    def get_product(self):
        return self.__product

    def set_product(self, product):
        self.__id_product = product.id


    def get_quantity(self) -> int:
        return self.__quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        self.__quantity = quantity
