from typing import Any

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from config.data_base.database import Base


class Product(Base):
    __tablename__ = "product"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)
    __product_name = Column("product_name", String, nullable=False)
    __unit_value = Column("unit_value", Float, nullable=False)
    __product_category_id = Column("product_category_id",Integer,ForeignKey("product_category.id"),nullable=False)
    __category = relationship("ProductCategory",back_populates="_ProductCategory__products")
    __stock_item = relationship("StockProduct",back_populates="_StockProduct__product",uselist=False)
    __active = Column("active", Boolean, nullable=False, default=True)

    def __init__(self,product_name: str,value: float,category,**kw: Any):
        super().__init__(**kw)
        self.__product_name = product_name
        self.__unit_value = value
        self.__category = category
        self.__active = True

        if category is not None:
            self.__product_category_id = category.get_id()

    @staticmethod
    def from_dict(data: dict) -> "Product":
        product = Product(
            data["product_name"],
            data["unit_value"],
            category=None
        )
        product.__product_category_id = data["product_category_id"]
        product.__id = data.get("id")
        product.__active = data.get("active", True)

        return product

    def to_dict(self) -> dict:
        return {
            "product_name": self.__product_name,
            "unit_value": self.__unit_value,
            "product_category_id": self.__product_category_id,
            "active": self.__active
        }

    def get_id(self):
        return self.__id

    def get_product_name(self) -> str:
        return self.__product_name

    def set_product_name(self, product_name: str):
        self.__product_name = product_name

    def get_unit_value(self) -> float:
        return self.__unit_value

    def set_unit_value(self, unit_value: float):
        self.__unit_value = unit_value

    def get_product_category(self):
        return self.__category

    def set_product_category_id(self, category):
        self.__category = category

    def get_stock_item(self):
        return self.__stock_item

    def set_stock_item(self, stock_item):
        self.__stock_item = stock_item

    def get_active(self) -> bool:
        return self.__active

    def set_active(self, active: bool):
        self.__active = active