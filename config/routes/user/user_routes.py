from config.routes.api_routes import ApiRoutes

class UserRoutes(ApiRoutes):
    USER_ROUTE = '/user'
    USER_PREFIX = ApiRoutes.API_PREFIX + USER_ROUTE