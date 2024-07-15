import Grafo
from typing import Tuple, List


def DFS(
    grafo: Grafo,
    ride: int,
    tempo: int,
    nota: int,
    caminho: List[int],
    melhorCaminho: List[int],
    melhorNota: int,
) -> Tuple[int, List[int]]:

    # Condição de parada
    if tempo <= 0:
        return 0, []

    caminho.append(ride)

    if nota > melhorNota:
        melhorNota = nota
        melhorCaminho[:] = caminho[:]

    for vizinho, duracao, notaVizinho in grafo.grafo[ride]:
        melhorNota, melhorCaminho = DFS(
            grafo,
            vizinho,
            tempo - duracao,
            nota + notaVizinho,
            caminho,
            melhorCaminho,
            melhorNota,
        )

    caminho.pop()
    return melhorNota, melhorCaminho
