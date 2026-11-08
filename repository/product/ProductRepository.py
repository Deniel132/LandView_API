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