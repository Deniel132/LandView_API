from config.data_base.database import supabase
from model.stock_exit_register import StockExitRegister


class StockExitRegisterRepository:

    @staticmethod
    def save_register(register: StockExitRegister):
        response = (supabase.table("stock_exit_register").insert(register.to_dict()).execute())
        if not response.data:
            return None
        return StockExitRegister.from_dict(response.data[0])

    @staticmethod
    def find_by_id(register_id: int):
        response = (supabase.table("stock_exit_register").select("*").eq("id", register_id).execute())

        if not response.data:
            return None

        return StockExitRegister.from_dict(response.data[0])

    @staticmethod
    def get_paged(page:int, page_size: int,  id_product:int | None = None, id_stock:int | None = None, id_user:int | None = None ):
        start = (page - 1) * page_size
        end = start + page_size -1
        query = supabase.table("stock_exit_register").select("*")

        if id_product:
            query =  query.eq("id_product", id_product)

        if id_stock:
            query = query.eq("id_stock", id_stock)

        if id_user:
            query = query.eq("id_user", id_user)

        response = (
            query
            .order("id", desc=True)
            .range(start, end)
            .execute()
        )

        if not response.data:
            return None

        mapped_response = []
        for resp in response.data:
            mapped_response.append(StockExitRegister.from_dict(resp))

        return mapped_response