from typing import Any

from sqlalchemy import Column, Integer, String, Boolean

from app.utils.token_utils import TokenUtils
from config.data_base.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    email = Column("email", String, nullable=False)
    password = Column("password", String, nullable=False)
    token = Column("token", String)
    role = Column("role", String)
    active = Column("active", Boolean, nullable=False, default=True)

    def __init__(self, email: str, password: str, token: str, role: str, **kw: Any):
        super().__init__(**kw)
        self.email = email
        self.password = password
        self.token = token
        self.role = role
        self.active = True

    @staticmethod
    def from_request_dto(user_request_dto):
        return User(user_request_dto.email, user_request_dto.password, user_request_dto.token, user_request_dto.role)

    def get_id(self):
        return self.id

    def set_email(self, email: str):
        self.email = email

    def get_email(self):
        return self.email


    def set_password(self, password: str):
        self.password = password

    def get_password(self):
        return self.password


    def set_token(self, token: str):
        self.token = token

    def get_token(self):
        return self.token


    def set_role(self, role: str):
        self.role = role

    def get_role(self):
        return self.role

    def set_active(self, active: bool):
        self.active = active

    def get_active(self):
        return self.active