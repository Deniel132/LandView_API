from infrastructure.erro.exceptions.conflict_exception import ConflictException
from infrastructure.erro.exceptions.bad_request_exception import BadRequestException
from infrastructure.erro.exceptions.not_found_exception import NotFoundException

from app.utils.password_utils import PasswordUtils
from app.utils.token_utils import TokenUtils
from dto.user.request.UserLoginDTO import UserLoginDTO
from dto.user.request.UserRequestDTO import UserRequestDTO
from dto.user.response.UserResponseDTO import UserResponseDTO
from model.user import User
from repository.user.UserRepository import UserRepository
from model.enums.user_role import UserRole


class UserService:
    repository = UserRepository()

    def find_by_id(self, user_id: int) -> UserResponseDTO:
        user = self.__get_by_id(user_id)
        if not user:
            raise NotFoundException
        return UserResponseDTO.from_user(user)

    def exist_by_email(self, email: str, user_id: int| None) -> bool:
        if user_id is None:
            return self.repository.exist_email(email)

        return self.repository.exist_email_for_dif_user(email, user_id)

    def create_user(self, user_dto: UserRequestDTO) -> UserResponseDTO:
        if user_dto.password is None or not user_dto.email:
            raise BadRequestException("Email ou senha não informado")

        if self.exist_by_email(user_dto.email, None):
            raise ConflictException("Email informado ja existente")

        if user_dto.role is None:
            user_dto.role = UserRole.USER

        user_dto.password = PasswordUtils.encode_password(user_dto.password)
        user = User.from_request_dto(user_dto)
        user = self.repository.save_user(user)

        return UserResponseDTO.from_user(user)


    def update_user(self, user_id: int, user_dto: UserRequestDTO) -> UserResponseDTO:
        if user_dto.password is None or not user_dto.email:
            raise BadRequestException("Email ou senha não informado")

        user = self.__get_by_id(user_id)
        if not user:
            raise BadRequestException("Usuário não encontrado")

        user.set_email(user_dto.email)
        user.set_role(user_dto.role.name)
        user.set_password(user_dto.password)
        self.repository.update_user(user_id,user)

        return UserResponseDTO.from_user(user)

    def delete_by_id(self, user_id: int):
        self.repository.delete_by_id(user_id)

        return "Usuario deletado"

    def __get_by_id(self, user_id: int) -> User:
        return self.repository.find_by_id(user_id)

    def login(self, user_login_dto: UserLoginDTO) -> str:
        user = self.repository.find_by_email(user_login_dto.email)

        if not user:
            raise BadRequestException("Email ou senha invalidos")

        has_valid_password = PasswordUtils.verify_password(user.get_password(), user_login_dto.password)

        if not has_valid_password:
            raise BadRequestException("Email ou senha invalidos")

        new_token = TokenUtils.generate_token(user.get_email())
        user.set_token(new_token)
        self.repository.update_user(user.get_id(), user)

        return new_token
