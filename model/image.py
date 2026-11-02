from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ImageBucket(Base):
    __tablename__ = 'image'
    __table_args__ = "schema: storage"

    __id = Column(Integer, primary_key=True)
    __image_name = Column(String, nullable=False)
    __content = Column(String, nullable=False)


    def __init__(self, image_name, content, **kw: Any):
        super().__init__(**kw)
        self.__image_name = image_name
        self.__content = content

    @staticmethod
    def from_dict(data: dict) -> "ImageBucket":
        return ImageBucket(image_name=data["image_name"], content=data["content"])

    def to_dict(self) -> dict:
        return {
            "image_name": self.__image_name,
            "content": self.__content
        }



    def get_image_name(self) -> str:
        return self.__image_name

    def get_content(self) -> str:
        return self.__content

    def set_image_name(self, image_name: str):
        self.__image_name = image_name
        return self

    def set_content(self, content: str):
        self.__content = content
        return self

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id
        return self

