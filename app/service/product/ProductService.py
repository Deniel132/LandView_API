from repository.product.ProductRepository import ProductRepository


class ProductService:
    repository = ProductRepository()


    @staticmethod
    def __get_by_id(self, product_id):
        return self.repository.find_by_id(product_id)

    @staticmethod
    def delete_by_id(self, user_id: int):
        self.repository.delete_by_id(user_id)
        return "Produto deletado"

