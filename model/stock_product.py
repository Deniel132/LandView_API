from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from config.data_base.database import Base
from model.product import Product


class StockProduct(Base):
    __tablename__ = "stock_product"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)
    __id_product = Column("id_product",Integer,ForeignKey("product.id"),nullable=False,unique=True)
    __quantity = Column("quantity", Integer, nullable=False, default=0)
    __product = relationship("Product", back_populates="_Product__stock_item")

    def __init__(self, id_product: int, quantity: int, id: int = None, **kw):
        super().__init__(**kw)
        self.__id = id
        self.__id_product = id_product
        self.__quantity = quantity

    @staticmethod
    def from_dict(data: dict) -> "StockProduct":
        return StockProduct(
            id_product=data["id_product"],
            quantity=data["quantity"],
            id=data.get("id")
        )
    def to_dict(self) -> dict:
        product_id = self.__id_product

        if isinstance(product_id, Product):
            product_id = product_id.get_id()

        return {
            "id_product": product_id,
            "quantity": self.__quantity
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
