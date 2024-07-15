from Grafo import Grafo
from DFS import DFS
from typing import List


def otimizar(atracoes: int, tempo_disp: int, duracoes_notas: List[List[int]]):
    grafo = Grafo(atracoes, duracoes_notas)
    melhorNota, melhorCaminho = DFS(grafo, atracoes, tempo_disp, 0, [], [], 0)
    return melhorNota, melhorCaminho
