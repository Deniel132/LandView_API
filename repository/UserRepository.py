from config.data_base.database import supabase
from model.user import User


class UserRepository:

    @staticmethod
    def find_by_id(self,user_id : int):
        response = (supabase.table("user").select("*").eq("id", user_id).execute())
        return response

    @staticmethod
    def find_by_token(self,token : str):
        response = (supabase.table("user").select("*").eq("token", token).execute())
        return response

    @staticmethod
    def delete_by_id(self,user_id : int):
        response = (supabase.table("user").where("id", user_id).delete())
        return response

    @staticmethod
    def save_user(self,user : User):
        response = (supabase.table("user").insert(user).execute())
        return response

    @staticmethod
    def update_user(self,user : User):
        response = (supabase.table("user").update(user).execute())
        return response