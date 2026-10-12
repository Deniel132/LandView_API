from app.utils.password_utils import PasswordUtils
from dto.user.request.UserRequestDTO import UserRequestDTO
from dto.user.response.UserResponseDTO import UserResponseDTO
from model.user import User
from repository.UserRepository import UserRepository
from model.enums.user_role import UserRole


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def find_by_id(self, user_id: int) -> UserResponseDTO:
        return UserResponseDTO.from_user(self.__get_by_id(user_id))

    def exist_by_email(self, email: str, user_id: int| None) -> bool:
        if user_id is None:
            return self.repository.exist_email(email)

        return self.repository.exist_email_for_dif_user(email, user_id)

    def create_user(self, user_dto: UserRequestDTO) -> UserResponseDTO:
        if user_dto.password is None or not user_dto.email:
            raise ValueError("Email ou senha não informado")

        if self.exist_by_email(user_dto.email, None):
            raise ValueError("Email informado ja existente")

        if user_dto.role is None:
            user_dto.role = UserRole.USER

        user = User.from_request_dto(user_dto)
        self.repository.save_user(user)

        return UserResponseDTO.from_user(user)


    def update_user(self, user_id: int, user_dto: UserRequestDTO) -> UserResponseDTO:
        if user_dto.password is None or not user_dto.email:
            raise ValueError("Email ou senha não informado")

        user = self.__get_by_id(user_id)
        user.set_email(user_dto.email)
        user.set_role(user_dto.role.name)
        user.set_password(PasswordUtils.encode_password(user_dto.password))
        self.repository.update_user(user)

        return UserResponseDTO.from_user(user)


    def __get_by_id(self, user_id: int) -> User:
        return self.repository.find_by_id(user_id)


