from config.routes.api_routes import ApiRoutes

class ProductRoutes(ApiRoutes):
    DASHBOARD_ROUTE = '/dashboard'
    DASHBOARD_PREFIX = ApiRoutes.API_PREFIX + DASHBOARD_ROUTE