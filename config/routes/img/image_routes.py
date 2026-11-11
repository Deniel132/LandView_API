from config.routes.api_routes import ApiRoutes

class ProductRoutes(ApiRoutes):
    IMAGE_ROUTE = '/image'
    IMAGE_PREFIX = ApiRoutes.API_PREFIX + IMAGE_ROUTE