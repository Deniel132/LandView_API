from config.routes.api_routes import ApiRoutes

class ProductRoutes(ApiRoutes):
    CATEGORY_ROUTE = '/category'
    CATEGORY_PREFIX = ApiRoutes.API_PREFIX + CATEGORY_ROUTE