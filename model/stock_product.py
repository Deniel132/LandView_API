
from typing import Optional

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from config.data_base.database import Base


class StockProduct(Base):
    __tablename__ = "stock_product"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)

    __id_product = Column(
        "id_product",
        Integer,
        ForeignKey("product.id"),
        nullable=False
    )

    __characteristics = Column("characteristics", String, nullable=True)
    __sub_characteristics = Column("sub_characteristics", String, nullable=True)
    __quantity = Column("quantity", Integer, nullable=False, default=0)

    __product = relationship(
        "Product",
        back_populates="_Product__stock_item"
    )

    def __init__(
        self,
        id_product: int,
        quantity: int = 0,
        characteristics: Optional[str] = None,
        sub_characteristics: Optional[str] = None,
        id: Optional[int] = None,
        **kw
    ):
        super().__init__(**kw)

        self.__id = id
        self.__id_product = id_product
        self.__quantity = quantity
        self.__characteristics = characteristics
        self.__sub_characteristics = sub_characteristics

    @staticmethod
    def from_dict(data: dict) -> "StockProduct":
        return StockProduct(
            id_product=data["id_product"],
            quantity=data.get("quantity", 0),
            characteristics=data.get("characteristics"),
            sub_characteristics=data.get("sub_characteristics"),
            id=data.get("id")
        )

    def to_dict(self) -> dict:
        return {
            "id_product": self.__id_product,
            "quantity": self.__quantity,
            "characteristics": self.__characteristics,
            "sub_characteristics": self.__sub_characteristics
        }

    def get_id(self) -> Optional[int]:
        return self.__id

    def get_product_id(self) -> int:
        return self.__id_product

    def get_product(self):
        return self.__product

    def set_product(self, product):
        self.__product = product

    def get_characteristics(self) -> Optional[str]:
        return self.__characteristics

    def set_characteristics(self, characteristics: Optional[str]):
        self.__characteristics = characteristics

    def get_sub_characteristics(self) -> Optional[str]:
        return self.__sub_characteristics

    def set_sub_characteristics(
        self,
        sub_characteristics: Optional[str]
    ):
        self.__sub_characteristics = sub_characteristics

    def get_quantity(self) -> int:
        return self.__quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        self.__quantity = quantity
