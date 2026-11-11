from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.data_base.database import Base


class Image(Base):

    __tablename__ = "image"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)
    __image_name = Column("image_name", String, nullable=False)
    __image_path = Column("image_path", String, nullable=False)
    __product_id = Column("product_id",Integer,ForeignKey("product.id"),nullable=False)
    __product = relationship("Product",back_populates="_Product__images")

    def __init__(self, image_name, image_path, product_id):
        self.__image_name = image_name
        self.__image_path = image_path
        self.__product_id = product_id

    def get_id(self):
        return self.__id

    def get_image_name(self) -> str:
        return self.__image_name

    def set_image_name(self, image_name: str):
        self.__image_name = image_name

    def get_image_path(self) -> str:
        return self.__image_path

    def set_image_path(self, image_path: str):
        self.__image_path = image_path

    def get_product_id(self) -> int:
        return self.__product_id

    def set_product_id(self, product_id: int):
        self.__product_id = product_id

    def get_product(self):
        return self.__product

    def set_product(self, product):
        self.__product = product