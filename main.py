from fastapi.middleware.cors import CORSMiddleware
from fastapi import *
from pydantic import BaseModel


app = FastAPI()


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


