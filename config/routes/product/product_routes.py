from config.routes.api_routes import ApiRoutes

class ProductRoutes(ApiRoutes):
    PRODUCT_ROUTE = '/product'
    PRODUCT_PREFIX = ApiRoutes.API_PREFIX + PRODUCT_ROUTE