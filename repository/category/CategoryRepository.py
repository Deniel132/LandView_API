from unicodedata import category

from config.data_base.database import supabase
from model.product_category import ProductCategory


class CategoryRepository:

    @staticmethod
    def find_by_id(category_id : int):
        response = (supabase.table("product_category").select("*").eq("id", category_id).execute())
        if not response.data:
           return None
        return ProductCategory.from_dict(response.data[0])

    @staticmethod
    def delete_by_id(category_id : int):
        response = (supabase.table("product_category").delete().eq("id", category_id).execute())
        if not response.data:
           return None
        return ProductCategory.from_dict(response.data[0])

    @staticmethod
    def save_category(product_category : ProductCategory):
        response = (supabase.table("product_category").insert(product_category.to_dict()).execute())
        if not response.data:
           return None
        return ProductCategory.from_dict(response.data[0])

    @staticmethod
    def update_category(category_id:int,product_category : ProductCategory):
        response = (supabase.table("product_category").update(product_category.to_dict()).eq("id",category_id).execute())
        if not response.data:
           return None
        return ProductCategory.from_dict(response.data[0])