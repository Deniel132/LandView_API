import bcrypt


class PasswordUtils:
    @staticmethod
    def encode_password(password: str):
        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password(hashed_password: str, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))