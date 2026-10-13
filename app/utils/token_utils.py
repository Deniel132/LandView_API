import secrets
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv


class TokenUtils:
    load_dotenv()

    @staticmethod
    def generate_token(email: str):
        crypto_email = TokenUtils.__encrypt_email(email)
        return secrets.token_urlsafe(16) + crypto_email

    @staticmethod
    def find_user_email(token: str):
        return TokenUtils.__decrypt_email(token[22:])

    @staticmethod
    def __encrypt_email(email: str):
        key = os.environ.get("ENCRYPT_KEY")
        fernet = Fernet(key)
        return fernet.encrypt(email.encode("utf-8")).decode("utf-8")

    @staticmethod
    def __decrypt_email(crypto_email: str):
        key = os.environ.get("ENCRYPT_KEY")
        fernet = Fernet(key)
        return fernet.decrypt(crypto_email.encode("utf-8")).decode("utf-8")