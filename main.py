from fastapi.middleware.cors import CORSMiddleware
from fastapi import *
from unicodedata import category

from config.routes.product import product_routes
from controller.category.category_controller import category_router
from model import product
from model.product import Product
from model.product_category import ProductCategory
from model.stock_product import StockProduct
from controller.stock.stock_controller import stock_router
from controller.product.product_controller import product_router
app = FastAPI()

from config.data_base.database import Base, Engine
from controller.user.user_controller import user_router

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE",  "OPTIONS"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=Engine)
app.include_router(user_router)
app.include_router(stock_router)
app.include_router(product_router)
app.include_router(category_router)

#python -m uvicorn main:app --reload