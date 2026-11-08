from psycopg.types import none

from config.data_base.database import supabase
from model.product import Product


class ProductRepository:

    @staticmethod
    def get_best_selling_products():

        response = supabase.table("stock_exit_register").select("*").execute()

        if not response.data:
            return []

        sales = {}

        for product in response.data:
            product_id = product["id_product"]
            sales[product_id] = sales.get(product_id, 0) + product["quantity"]

        best_selling = sorted(sales.items(), key=lambda item: item[1], reverse=True)

        result = []

        for product_id, total_sold in best_selling:
            product_response = supabase.table("product").select("*").eq("id", product_id).execute()

            if product_response.data:
                product = product_response.data[0]
                unit_value = product["unit_value"]

                result.append({
                    "id": product["id"],
                    "product_name": product["product_name"],
                    "unit_value": unit_value,
                    "total_sold": total_sold,
                    "total_value": product["unit_value"] * total_sold
                })

        return result

    @staticmethod
    def get_all() -> list[Product]:
        response = (supabase.table("product").select("*").execute())

        if not response.data:
            return []

        mapped_response = []
        for resp in response.data:
            mapped_response.append(Product.from_dict(resp))

        return mapped_response

    @staticmethod
    def get_filtered_products(
            page:int,
            page_size: int,
            id_product:int | None = None,
            id_stock:int | None = None,
            unit_value: float | None = None,
            id_category:int | None = None,
            active:bool | None = None,
            name:str | None = None
    ) -> list[Product]:
        start = (page - 1) * page_size
        end = start + page_size - 1
        query = None
        if id_stock and id_stock is not None:
            query = supabase.table("product").select("*, stock_product!inner(*)").eq("stock_product.id", id_stock)
        else:
            query = supabase.table("product").select("*")

        if id_product and id_product is not None:
            query = query.eq("id", id_product)

        if unit_value and unit_value is not None:
            query = query.eq("unit_value", unit_value)

        if id_category and id_category is not None:
            query = query.eq("product_category_id", id_category)

        if name and name is not None:
            query = query.ilike("product_name", name)

        if active  is not None:
            query = query.eq("active", active)

        response = (
            query
            .order("id", desc=True)
            .range(start, end)
            .execute()
        )

        if not response.data:
            return []

        product_list = []
        for resp in response.data:
            product_list.append(Product.from_dict(resp))

        return product_list

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
    def update_product(product_id:int,product : Product):
        response = (supabase.table("product").update(product.to_dict()).eq("id",product_id).execute())
        if not response.data:
           return None
        return Product.from_dict(response.data[0])