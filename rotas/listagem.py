from fastapi import APIRouter
from models import TarefaSaida
from storage import tarefas

router = APIRouter()


@router.get("/", response_model=list[TarefaSaida])
def listar_tarefas(concluida: bool | None = None):
    resultado = list(tarefas.values())

    if concluida is not None:
        resultado = [
            tarefa for tarefa in resultado
            if tarefa.concluida == concluida
        ]

    return resultado
