from typing import Any

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.data_base.database import Base


class ProductCategory(Base):
    __tablename__ = "product_category"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)
    __category_name = Column("category_name", String, nullable=False)
    __category_type = Column("category_type", String, nullable=False)
    __products = relationship("Product",back_populates="_Product__category")


    def __init__(self, category_name, category_type, **kw: Any):
        super().__init__(**kw)
        self.__category_name = category_name
        self.__category_type = category_type

    @staticmethod
    def from_request_dto(category_request_dto):
        return ProductCategory(
            category_request_dto.category_name,
            category_request_dto.category_type
        )
    @staticmethod
    def from_dict(data: dict) -> "ProductCategory":
        category = ProductCategory(
            category_name=data["category_name"],
            category_type=data["category_type"]
        )
        category.__id = data.get("id")

        return category

    def to_dict(self) -> dict:
        return {
            "category_name": self.__category_name,
            "category_type": self.__category_type
            }

    def get_id(self):
        return self.__id

    def get_category_name(self) -> str:
        return self.__category_name

    def set_category_name(self, category_name: str):
        self.__category_name = category_name

    def get_category_type(self) -> str:
        return self.__category_type

    def set_category_type(self, category_type: str):
        self.__category_type = category_type