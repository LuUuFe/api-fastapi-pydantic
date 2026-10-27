from pydantic import BaseModel, Field


class TarefaEntrada(BaseModel):
    titulo: str = Field(min_length=3, max_length=100)
    descricao: str | None = None
    concluida: bool = False


class TarefaSaida(TarefaEntrada):
    id: int
