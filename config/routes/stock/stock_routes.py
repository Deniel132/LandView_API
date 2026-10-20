from config.routes.api_routes import ApiRoutes

class StockRoutes(ApiRoutes):
    STOCK_ROUTE = '/stock'
    STOCK_PREFIX = ApiRoutes.API_PREFIX + STOCK_ROUTE