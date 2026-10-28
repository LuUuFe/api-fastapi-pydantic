from fastapi import APIRouter, HTTPException, status
from storage import tarefas

router = APIRouter()


@router.delete(
    "/{tarefa_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def excluir_tarefa(tarefa_id: int):
    if tarefa_id not in tarefas:
        raise HTTPException(
            status_code=404,
            detail="Tarefa nao encontrada"
        )

    tarefas.pop(tarefa_id)
