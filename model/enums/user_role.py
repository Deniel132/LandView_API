from enum import Enum
from typing import Any


class UserRole(Enum):
    SELLER = "seller"
    OWNER = "owner"
    USER = "user"


    @classmethod
    def _missing_(cls,value):
        if isinstance(value,str):
            return Role_Lookup.get(value.lower())
        return None

Role_Lookup = {role.value.lower(): role for role in UserRole}