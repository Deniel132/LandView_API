from config.data_base.database import supabase
from model.user import User


class UserRepository:

    @staticmethod
    def find_by_id(user_id : int):
        response = (supabase.table("user").select("*").eq("id", user_id).execute())
        if not response.data:
           return None
        return User.from_dict(response.data[0])

    @staticmethod
    def find_by_token(token : str):
        response = (supabase.table("user").select("*").eq("token", token).execute())
        if not response.data:
           return None
        return User.from_dict(response.data[0])

    @staticmethod
    def delete_by_id(user_id : int):
        response = (supabase.table("user").delete().eq("id", user_id).execute())
        if not response.data:
           return None
        return User.from_dict(response.data[0])

    @staticmethod
    def save_user(user : User):
        response = (supabase.table("user").insert(user.to_dict()).execute())
        if not response.data:
           return None
        return User.from_dict(response.data[0])

    @staticmethod
    def update_user(user : User):
        response = (supabase.table("user").update(user.to_dict()).execute())
        if not response.data:
           return None
        return User.from_dict(response.data[0])

    @staticmethod
    def exist_email(email: str):
        response = (supabase.table("user").select("*").eq("email", email).execute())
        return len(response.data) > 0

    @staticmethod
    def exist_email_for_dif_user(email: str, user_id : int):
        response = (supabase.table("user").select("*").eq("email", email).neq("id", user_id).execute())
        return len(response.data) > 0