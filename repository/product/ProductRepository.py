from config.data_base.database import supabase
from model.product import Product


class ProductRepository:

    @staticmethod
    def find_by_id(product_id : int):
        response = (supabase.table("product").select("*").eq("id", product_id).execute())
        if not response.data:
           return None
        return Product.from_dict(response.data[0])

    @staticmethod
    def delete_by_id(product_id : int):
        response = (supabase.table("product").delete().eq("id", product_id).execute())
        if not response.data:
           return None
        return Product.from_dict(response.data[0])

    @staticmethod
    def save_product(product : Product):
        response = (supabase.table("product").insert(product.to_dict()).execute())
        if not response.data:
           return None
        return Product.from_dict(response.data[0])

    @staticmethod
    def update_product(product : Product):
        response = (supabase.table("product").update(product.to_dict()).execute())
        if not response.data:
           return None
        return Product.from_dict(response.data[0])