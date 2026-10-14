from typing import Any

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.data_base.database import Base


class ProductCategory(Base):
    __tablename__ = "product_category"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)
    __category_name = Column("product_name", String)
    __category_type = Column("category_type", String)
    __products = relationship("Product",back_populates="_Product__category")


    def __init__(self, category_name, category_type, **kw: Any):
        super().__init__(**kw)
        self.category_name = category_name
        self.category_type = category_type


    def get_id(self) -> Column[int]:
        return self.__id

    def get_product_name(self) -> str:
        return self.__category_name

    def set_product_name(self, product_name: str):
        self.__category_name = product_name

    def get_category_type(self) -> str:
        return self.__category_type

    def set_category_type(self, category_type: str):
        self.__category_type = category_type