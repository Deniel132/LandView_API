
from pydantic import BaseModel


class ImageResponseDTO(BaseModel):
    image_id: int
    image_name: str
    image_url: str

    @staticmethod
    def from_dict(image: dict, image_url: str):
        return ImageResponseDTO(
            image_id=image["id"],
            image_name=image["image_name"],
            image_url=image_url
        )
