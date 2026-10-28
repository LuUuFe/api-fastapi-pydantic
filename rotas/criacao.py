from fastapi import APIRouter, status
from models import TarefaEntrada, TarefaSaida
from storage import tarefas, gerador_id

router = APIRouter()


@router.post(
    "/",
    response_model=TarefaSaida,
    status_code=status.HTTP_201_CREATED
)
def criar_tarefa(dados: TarefaEntrada):
    novo_id = next(gerador_id)

    nova_tarefa = TarefaSaida(
        id=novo_id,
        **dados.model_dump()
    )

    tarefas[novo_id] = nova_tarefa

    return nova_tarefa
