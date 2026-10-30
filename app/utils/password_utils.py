import os
import secrets
import bcrypt
from dotenv import load_dotenv

load_dotenv()


class PasswordUtils:
    _PREFIX = "enc:v1:"
    _DEFAULT_KEY = "yEAMz6EQ0uo6YD7AM8dCZiGRkqfd9iFO1wqaObFj1VQ="

    @staticmethod
    def _get_key_bytes() -> bytes:
        key = os.getenv("ENCRYPT_KEY") or PasswordUtils._DEFAULT_KEY
        return key.encode("utf-8")

    @staticmethod
    def encrypt_client_password(password: str) -> str:
        """Criptografa a senha no mesmo formato enviado pelo frontend Flutter."""
        if password.startswith(PasswordUtils._PREFIX):
            return password
        key_bytes = PasswordUtils._get_key_bytes()
        nonce = secrets.token_bytes(8)
        plain_bytes = password.encode("utf-8")
        cipher = bytearray(len(plain_bytes))
        for i, b in enumerate(plain_bytes):
            mask = (
                key_bytes[i % len(key_bytes)]
                ^ nonce[i % 8]
                ^ ((i * 31 + 17) & 0xFF)
            ) & 0xFF
            cipher[i] = b ^ mask
        return PasswordUtils._PREFIX + (bytes(nonce) + bytes(cipher)).hex()

    @staticmethod
    def decrypt_client_password(password: str) -> str:
        """Reverte a senha criptografada pelo frontend (enc:v1:...) antes do bcrypt."""
        if not password or not password.startswith(PasswordUtils._PREFIX):
            return password
        raw = bytes.fromhex(password[len(PasswordUtils._PREFIX) :])
        if len(raw) < 8:
            raise ValueError("Formato de senha criptografada inválido.")
        nonce = raw[:8]
        cipher = raw[8:]
        key_bytes = PasswordUtils._get_key_bytes()
        plain = bytearray(len(cipher))
        for i, b in enumerate(cipher):
            mask = (
                key_bytes[i % len(key_bytes)]
                ^ nonce[i % 8]
                ^ ((i * 31 + 17) & 0xFF)
            ) & 0xFF
            plain[i] = b ^ mask
        return bytes(plain).decode("utf-8")

    @staticmethod
    def encode_password(password: str):
        plain_password = PasswordUtils.decrypt_client_password(password)
        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password(hashed_password: str, password: str):
        plain_password = PasswordUtils.decrypt_client_password(password)
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password.encode("utf-8")
        )
