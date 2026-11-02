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