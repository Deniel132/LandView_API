from app.service.img.ImageService import ImageService
from dto.product.request.CreateProductRequestDTO import CreateProductRequestDTO
from dto.product.request.ProductRequestDTO import ProductRequestDTO
from dto.product.response.ProductResponseDTO import ProductResponseDTO
from model.product import Product
from repository.category.CategoryRepository import CategoryRepository
from repository.product.ProductRepository import ProductRepository
from infrastructure.erro.exceptions.not_found_exception import NotFoundException
from infrastructure.erro.exceptions.bad_request_exception import BadRequestException

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()
        self.category_repository = CategoryRepository()
        self.image_service = ImageService()

    def get_all_products(self):
        response = self.repository.get_all()

        if not response:
            return []

        product_list = []
        for resp in response:
            product_list.append(ProductResponseDTO.from_product(resp))

        return product_list

    def get_filtered_products(self, page:int = 1, page_size: int = 10, id_product:int | None = None, id_stock:int | None = None, unit_value: float | None = None,  id_category:int | None = None,  active:bool | None = None,  name:str | None = None):
        if page < 1 or page_size < 1:
            raise BadRequestException("Pagina ou tamanho de pagina incorreto")

        response = self.repository.get_filtered_products(page, page_size, id_product, id_stock, unit_value, id_category, active, name)

        if not response:
            return []

        product_list = []
        for resp in response:
            product_list.append(ProductResponseDTO.from_product(resp))

        return product_list

    def __get_by_id(self, product_id):
        return self.repository.find_by_id(product_id)

    def find_by_id(self, product_id):
        product = self.__get_by_id(product_id)

        if product is None:
            raise NotFoundException("Produto não encontrado")

        return ProductResponseDTO.from_product(product)

    def create_product(self, request: CreateProductRequestDTO):
        category = self.category_repository.find_by_id(request.category_id)

        if category is None:
            raise NotFoundException("Categoria não encontrada")

        product = Product(request.product_name, request.unit_value, category)
        saved_product = self.repository.save_product(product)

        if request.images:
            self.image_service.create_files(
                saved_product.get_id(),
                request.images
            )

        return ProductResponseDTO.from_product(saved_product)

    def update_product(self, product_id: int,request:ProductRequestDTO):
        product = self.__get_by_id(product_id)

        if product is None:
            raise NotFoundException("Produto não encontrado")

        category = self.category_repository.find_by_id(request.product_category_id)

        if category is None:
            raise NotFoundException("Categoria não encontrada")

        product.set_product_name(request.product_name)
        product.set_unit_value(request.unit_value)
        product.set_category_id(category)

        updated_product = self.repository.update_product(product_id, product)

        if updated_product is None:
            raise BadRequestException("Não foi possível atualizar o produto")

        return ProductResponseDTO.from_product(updated_product)


    def delete_by_id(self, user_id: int):
        self.repository.delete_by_id(user_id)
        return "Produto deletado"


