from fastapi.middleware.cors import CORSMiddleware
from fastapi import *

from controller.category.category_controller import category_router
from controller.stock.stock_controller import stock_router
from controller.product.product_controller import product_router
app = FastAPI()

from config.data_base.database import Base, Engine
from controller.user.user_controller import user_router, user_public_router

app.add_middleware(
    CORSMiddleware,
    allow_origins=[''
        "https://landview-frontstack.agendamentoapi-14e.workers.dev/"
    ],
    allow_origin_regex=r"^http://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=Engine)
app.include_router(user_router)
app.include_router(stock_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(user_public_router)


#python -m uvicorn main:app --reload