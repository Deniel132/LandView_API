from pydantic import BaseModel


class ImageRequestDTO(BaseModel):
    images: list[str]