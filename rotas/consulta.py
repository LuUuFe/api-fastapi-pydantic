from fastapi import APIRouter, HTTPException
from models import TarefaSaida
from storage import tarefas

router = APIRouter()


@router.get("/{tarefa_id}", response_model=TarefaSaida)
def buscar_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(
            status_code=404,
            detail="Tarefa nao encontrada"
        )

    return tarefas[tarefa_id]
