
# API de Gerenciamento de Tarefas

## Integrantes
- Luis Felipe Andrade Dias

## Sobre o projeto

API RESTful desenvolvida com Python, FastAPI e
Pydantic para gerenciamento de tarefas.

O sistema oferece operacoes de cadastro,
consulta, atualizacao e exclusao.

Os dados sao armazenados em memoria.

## Tecnologias

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

## Instalacao

Clone o repositorio:

git clone URL_DO_REPOSITORIO

Instale as dependencias:

pip install -r requirements.txt

Inicie o servidor:

uvicorn main:app --reload

## Documentacao

Swagger:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

## Endpoints

GET /tarefas/
- Listar todas as tarefas.

GET /tarefas/{tarefa_id}
- Buscar tarefa pelo ID.

POST /tarefas/
- Cadastrar nova tarefa.

PUT /tarefas/{tarefa_id}
- Atualizar tarefa existente.

DELETE /tarefas/{tarefa_id}
- Excluir tarefa.

## Exemplo de requisicao

{
    "titulo": "Estudar FastAPI",
    "descricao": "Realizar atividade da faculdade",
    "concluida": false
}

## Observacoes

O projeto utiliza armazenamento em memoria.
Ao reiniciar o servidor, as tarefas sao perdidas.

A validacao de entrada e saida e realizada
por modelos Pydantic.

A documentacao e gerada automaticamente
pelo FastAPI.