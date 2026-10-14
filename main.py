from fastapi.middleware.cors import CORSMiddleware
from fastapi import *
from pydantic import BaseModel
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
