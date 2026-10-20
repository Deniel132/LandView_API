from dto.category.request.CategoryRequestDTO import CategoryRequestDTO
from dto.category.response.CategoryResponseDTO import CategoryResponseDTO
from model.product_category import ProductCategory
from repository.category.CategoryRepository import CategoryRepository


class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()


    def __get_by_id(self, category_id: int):
        return self.repository.find_by_id(category_id)

    def find_by_id(self, category_id : int):
        category = self.__get_by_id(category_id)
        if category is None:
            raise ValueError("Categoria não encontrada")

        return CategoryResponseDTO.from_category(category)

    def create_category(self,request:CategoryRequestDTO)-> CategoryResponseDTO:
        category = ProductCategory.from_request_dto(request)
        saved_category = self.repository.save_category(category)



        return CategoryResponseDTO.from_category(saved_category)

    def update_category(self,category_id:int , request:CategoryRequestDTO):
        category = self.__get_by_id(category_id)

        if category is None:
            raise ValueError("Categoria não encontrada")

        category.set_category_name(request.category_name)
        category.set_category_type(request.category_type)
        updated_category = self.repository.update_category(category_id,category)
        if updated_category is None:
            raise ValueError("Categoria não atualizada")

        return CategoryResponseDTO.from_category(updated_category)

    def delete_category(self,category_id:int):
        category = self.repository.delete_by_id(category_id)
        if category is None:
            raise ValueError("Categoria nâo encontrada")

        return "Categoria removida com sucesso"

