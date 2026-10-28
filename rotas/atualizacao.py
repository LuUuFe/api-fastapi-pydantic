from fastapi import APIRouter, HTTPException
from models import TarefaEntrada, TarefaSaida
from storage import tarefas

router = APIRouter()


@router.put("/{tarefa_id}", response_model=TarefaSaida)
def atualizar_tarefa(tarefa_id: int, dados: TarefaEntrada):
    if tarefa_id not in tarefas:
        raise HTTPException(
            status_code=404,
            detail="Tarefa nao encontrada"
        )

    tarefa_atualizada = TarefaSaida(
        id=tarefa_id,
        **dados.model_dump()
    )

    tarefas[tarefa_id] = tarefa_atualizada

    return tarefa_atualizada
