
from config.data_base.database import supabase


class ImageRepository:

    BUCKET_NAME = "product-images"

    @staticmethod
    def upload(image_path: str, image_bytes: bytes, content_type: str):
        return supabase.storage.from_(
            ImageRepository.BUCKET_NAME
        ).upload(
            path=image_path,
            file=image_bytes,
            file_options={
                "content-type": content_type,
                "upsert": "false"
            }
        )

    @staticmethod
    def save_image(image_name: str, image_path: str, product_id: int):
        response = (
            supabase.table("image")
            .insert({
                "image_name": image_name,
                "image_path": image_path,
                "product_id": product_id
            })
            .execute()
        )

        return response.data[0] if response.data else None

    @staticmethod
    def find_by_id(image_id: int):
        response = (
            supabase.table("image")
            .select("*")
            .eq("id", image_id)
            .execute()
        )

        return response.data[0] if response.data else None

    @staticmethod
    def find_by_product_id(product_id: int):
        response = (
            supabase.table("image")
            .select("*")
            .eq("product_id", product_id)
            .execute()
        )

        return response.data

    @staticmethod
    def update_image(image_id: int, image_name: str, image_path: str):
        response = (
            supabase.table("image")
            .update({
                "image_name": image_name,
                "image_path": image_path
            })
            .eq("id", image_id)
            .execute()
        )

        return response.data[0] if response.data else None

    @staticmethod
    def delete_storage(image_path: str):
        return supabase.storage.from_(
            ImageRepository.BUCKET_NAME
        ).remove([image_path])

    @staticmethod
    def delete_image_record(image_id: int):
        response = (
            supabase.table("image")
            .delete()
            .eq("id", image_id)
            .execute()
        )

        return response.data[0] if response.data else None

    @staticmethod
    def get_public_url(image_path: str):
        return supabase.storage.from_(
            ImageRepository.BUCKET_NAME
        ).get_public_url(image_path)

    @staticmethod
    def find_by_filters(
            product_id: int,
            image_id: int | None = None,
            image_name: str | None = None
    ):
        query = (
            supabase.table("image")
            .select("*")
            .eq("product_id", product_id)
        )

        if image_id is not None:
            query = query.eq("id", image_id)

        if image_name:
            query = query.ilike("image_name", f"%{image_name}%")

        response = query.execute()
        return response.data