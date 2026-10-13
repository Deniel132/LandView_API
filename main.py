from fastapi.middleware.cors import CORSMiddleware
from fastapi import *
from pydantic import BaseModel
app = FastAPI()

from config.data_base.database import Base, Engine
from controller.user.user_controller import user_router
from model.user import User

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


clientes = []


class Cliente(BaseModel):
    nome: str
    email: str
    idade: int


@app.post("/clientes")
def adicionar_cliente(cliente: Cliente):
    clientes.append(cliente)

    return {
        "message": "Cliente adicionado",
        "cliente": cliente
    }


@app.get("/clientes")
def listar_clientes():
    return {
        "message": "Clientes encontrados",
        "clientes": clientes
    }

Base.metadata.create_all(bind=Engine)
app.include_router(user_router)
