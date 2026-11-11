from fastapi.middleware.cors import CORSMiddleware
from fastapi import *

from controller.category.category_controller import category_router
from controller.dashboard.dashboard_controller import dashboard_router
from controller.img.ImageController import image_router
from controller.stock.stock_controller import stock_router
from controller.product.product_controller import product_router
from controller.stock.stock_exit_controller import stock_exit_router
from controller.user.user_controller import user_router, user_public_router
from model.product import Product
from model.image import Image
from model.product_category import ProductCategory
from model.stock_product import StockProduct



from infrastructure.erro.global_heandler import GlobalHandler

from config.data_base.database import Base, Engine

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://landview.onrender.com"],
    allow_origin_regex=r"^http://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=Engine)

app.include_router(user_router)
app.include_router(stock_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(dashboard_router)
app.include_router(user_public_router)
app.include_router(stock_exit_router)
app.include_router(image_router)

GlobalHandler(app)

# Executar:
# python -m uvicorn main:app --reload