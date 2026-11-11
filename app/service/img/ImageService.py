
import base64
import binascii
from uuid import uuid4

from infrastructure.erro.exceptions.not_found_exception import NotFoundException
from repository.img.ImageRepository import ImageRepository


class ImageService:

    def __init__(self):
        self.repository = ImageRepository()

    def create_files(self, product_id: int, files_base64: list[str]):

        if not files_base64:
            raise ValueError("Nenhum arquivo foi enviado")

        saved_files = []

        for file_base64 in files_base64:

            try:
                file_bytes = base64.b64decode(file_base64, validate=True)
            except (binascii.Error, ValueError):
                raise ValueError("Arquivo Base64 inválido")

            if not file_bytes:
                raise ValueError("O arquivo está vazio")

            file_id = str(uuid4())
            file_path = f"products/{product_id}/{file_id}"

            # Salva o conteúdo Base64 no bucket
            self.repository.upload(
                file_path,
                file_base64.encode("utf-8"),
                "text/plain"
            )

            try:
                saved_file = self.repository.save_image(
                    file_id,
                    file_path,
                    product_id
                )

                if saved_file is None:
                    raise ValueError("Não foi possível salvar o arquivo")

                saved_files.append(saved_file)

            except Exception:
                self.repository.delete_storage(file_path)
                raise

        return saved_files

    def get_all_images_by_product(self,product_id: int):

        images = self.repository.find_by_product_id(product_id)

        if not images:
            return []

        image_list = []

        for image in images:
            image_list.append({
                "id": image["id"],
                "image_name": image["image_name"],
                "image_path": image["image_path"],
                "product_id": image["product_id"],
                "url": self.repository.get_public_url(image["image_path"])
            })

        return image_list

    def get_images_by_filters(
            self,
            product_id: int,
            image_id: int | None = None,
            image_name: str | None = None
    ):
        images = self.repository.find_by_filters(
            product_id,
            image_id,
            image_name
        )

        return [
            {
                "id": image["id"],
                "image_name": image["image_name"],
                "image_path": image["image_path"],
                "product_id": image["product_id"],
                "url": self.repository.get_public_url(image["image_path"])
            }
            for image in images
        ]

    def delete_file(self, product_id: int, image_id: int):

        image = self.repository.find_by_id(image_id)

        if image is None:
            raise NotFoundException("Imagem não encontrada")

        if image["product_id"] != product_id:
            raise NotFoundException("Imagem não pertence a este produto")

        self.repository.delete_storage(image["image_path"])

        self.repository.delete_image_record(image_id)

        return {"message": "Imagem excluída com sucesso"}