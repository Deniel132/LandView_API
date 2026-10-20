from typing import Any

from sqlalchemy import Column, Integer, String, Boolean

from app.utils.password_utils import PasswordUtils
from app.utils.token_utils import TokenUtils
from config.data_base.database import Base

class User(Base):
    __tablename__ = "user"

    __id = Column("id", Integer, primary_key=True, autoincrement=True)
    __email = Column("email", String, nullable=False, unique=True)
    __password = Column("password", String, nullable=False)
    __token = Column("token", String, unique=True)
    __role = Column("role", String)
    __active = Column("active", Boolean, nullable=False, default=True)

    def __init__(self, email: str, password: str, role: str, **kw: Any):
        super().__init__(**kw)
        self.__email = email
        self.__password = password
        self.__token = TokenUtils.generate_token(email)
        self.__role = role
        self.__active = True

    @staticmethod
    def from_request_dto(user_request_dto):
        return User(user_request_dto.email, user_request_dto.password, user_request_dto.role.name)

    @staticmethod
    def from_dict(data: dict) -> "User":
        user = User(data["email"], data["password"], data["role"])
        user.__id = data["id"]
        user.__token = data["token"]
        user.__active = data["active"]

        return user

    def to_dict(self) -> dict:
        return {
            "email": self.__email,
            "password": self.__password,
            "token": self.__token,
            "role": self.__role,
            "active": self.__active
        }

    def get_id(self):
        return self.__id

    def set_email(self, email: str):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_password(self, password: str):
        self.__password = PasswordUtils.encode_password(password)

    def get_password(self):
        return self.__password


    def set_token(self, token: str):
        self.__token = token

    def get_token(self):
        return self.__token


    def set_role(self, role: str):
        self.__role = role

    def get_role(self):
        return self.__role

    def set_active(self, active: bool):
        self.__active = active

    def get_active(self):
        return self.__active