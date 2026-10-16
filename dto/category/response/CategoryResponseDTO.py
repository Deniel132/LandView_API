from model.product_category import ProductCategory


class CategoryResponseDTO:
    def __init__(self,category_id: int, category_name: str, category_type: str):
        self.category_id = category_id
        self.category_name = category_name
        self.category_type = category_type



    @staticmethod
    def from_category(category:ProductCategory):
        return CategoryResponseDTO(category.get_id(), category.get_category_name(), category.get_category_type())