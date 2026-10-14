from config.data_base.database import supabase
from model.stock_product import StockProduct


class StockRepository:

    @staticmethod
    def find_by_id(stock_product_id: int):
        response = (supabase.table("stock_product").select("*").eq("id", stock_product_id).execute())

        if not response.data:
            return None

        return StockProduct.from_dict(response.data[0])

    @staticmethod
    def find_all():
        response = (supabase.table("stock_product").select("*").execute())

        if not response.data:
            return []

        return [StockProduct.from_dict(item) for item in response.data]

    @staticmethod
    def delete_by_id(stock_product_id: int):
        response = (supabase.table("stock_product").delete().eq("id",stock_product_id).execute())

        if not response.data:
            return None

        return StockProduct.from_dict(response.data[0])

    @staticmethod
    def save_stock_product(stock_product: StockProduct):
        response = (supabase.table("stock_product").insert(stock_product.to_dict()).execute())
        if not response.data:
            return None

        return StockProduct.from_dict(response.data[0])

    @staticmethod
    def update_stock_product(stock_product_id: int, stock_product: StockProduct):
        response = (supabase.table("stock_product").update(stock_product).eq("id",stock_product_id).execute())

        if not response.data:
            return None

        return StockProduct.from_dict(response.data[0])
