from dto.product.request.ProductRequestDTO import ProductRequestDTO
from dto.product.response.ProductResponseDTO import ProductResponseDTO
from model.product import Product
from repository.category.CategoryRepository import CategoryRepository
from repository.product.ProductRepository import ProductRepository


class ProductService:
    def __init__(self):
        self.repository = ProductRepository()
        self.category_repository = CategoryRepository()

    def __get_by_id(self, product_id):
        return self.repository.find_by_id(product_id)

    def find_by_id(self, product_id):
        product = self.__get_by_id(product_id)

        if product is None:
            raise ValueError("Produto não encontrado")

        return ProductResponseDTO.from_product(product)

    def create_product(self, request:ProductRequestDTO):
        category = self.category_repository.find_by_id(request.product_category_id)
        if category is None:
            raise ValueError("Categoria não encontrada")

        product = Product(request.product_name, request.unit_value, category)
        saved_product = self.repository.save_product(product)

        return ProductResponseDTO.from_product(saved_product)

    def update_product(self, product_id: int,request:ProductRequestDTO):
        product = self.find_by_id(product_id)

        if product is None:
            raise ValueError("Produto não encontrado")

        category = self.category_repository.find_by_id(request.product_category_id)

        if category is None:
            raise ValueError("Categoria não encontrada")

        product.set_product_name(request.product_name)
        product.set_unit_value(request.unit_value)
        product.set_category_id(category)

        updated_product = self.repository.update_product(product_id, product)

        if updated_product is None:
            raise ValueError("Não foi possível atualizar o produto")

        return ProductResponseDTO.from_product(updated_product)


    def delete_by_id(self, user_id: int):
        self.repository.delete_by_id(user_id)
        return "Produto deletado"


