from typing import Any

from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from config.data_base.database import Base


class StockProduct(Base):
    __tablename__ = "stock_product"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)
    __id_product = Column("id_product",Integer,ForeignKey("product.id"),nullable=False)
    __id_product_category = Column("id_product_category",Integer,ForeignKey("product_category.id"),nullable=False)
    __quantity = Column("quantity", Integer, nullable=False, default=0)
    __product = relationship("Product")
    __product_category = relationship("ProductCategory")
    __active = Column("active", Boolean, nullable=False, default=True)

    def __init__(self,product,product_category,quantity: int,**kw: Any):
        super().__init__(**kw)
        self.__product = product
        self.__product_category = product_category
        self.__quantity = quantity
        self.__active = True

    @staticmethod
    def from_dict(data: dict) -> "StockProduct":
        stock_product = StockProduct(
            data["product"],
            data["product_category"],
            data["quantity"]
        )
        stock_product.__id = data.get("id")
        stock_product.__active = data.get("active", True)

        return stock_product

    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "id_product": self.__id_product,
            "id_product_category": self.__id_product_category,
            "quantity": self.__quantity,
            "active": self.__active
        }

    def get_id(self):
        return self.__id

    def get_product(self):
        return self.__product

    def set_product(self, product):
        self.__product = product

    def get_product_category(self):
        return self.__product_category

    def set_product_category(self, product_category):
        self.__product_category = product_category

    def get_quantity(self) -> int:
        return self.__quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        self.__quantity = quantity

    def get_active(self) -> bool:
        return self.__active

    def set_active(self, active: bool):
        self.__active = active