
from fastapi import FastAPI

from rotas import (
    listagem,
    consulta,
    criacao,
    atualizacao,
    exclusao
)

app = FastAPI(
    title="API de Gerenciamento de Tarefas",
    description="API RESTful utilizando FastAPI e Pydantic.",
    version="1.0.0"
)


@app.get("/")
def inicio():
    return {
        "mensagem": "API de gerenciamento de tarefas funcionando!"
    }


# Registrando as rotas
app.include_router(
    listagem.router,
    prefix="/tarefas",
    tags=["Tarefas"]
)

app.include_router(
    consulta.router,
    prefix="/tarefas",
    tags=["Tarefas"]
)

app.include_router(
    criacao.router,
    prefix="/tarefas",
    tags=["Tarefas"]
)

app.include_router(
    atualizacao.router,
    prefix="/tarefas",
    tags=["Tarefas"]
)

app.include_router(
    exclusao.router,
    prefix="/tarefas",
    tags=["Tarefas"]
)
