from itertools import count
from models import TarefaSaida

# Dados armazenados em memoria
tarefas: dict[int, TarefaSaida] = {}

# Gerador de identificadores
gerador_id = count(1)
