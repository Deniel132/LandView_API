from pydantic import BaseModel


class CategoryRequestDTO(BaseModel):
    category_name: str
    category_type: str
