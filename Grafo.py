from typing import List


class Grafo:

    # Iniciando uma lista para cada vértice, mais um vértice raiz para a busca
    def __init__(self, tamanho: int, duracoes_notas: List[List[int]]) -> None:
        self.grafo = [[] for _ in range(tamanho + 1)]
        self.construir(duracoes_notas, tamanho)

    # Criando arestas com o peso de cada atração
    def construir(self, duracoes_notas: List[List[int]], tamanho: int) -> None:
        # enumerate separa elementos e os indexa.
        for i, duracao_nota in enumerate(duracoes_notas):
            duracao, nota = duracao_nota
            self.grafo[tamanho].append([i, duracao, nota])  # Conectando à raiz
            for j, duracao_nota_j in enumerate(duracoes_notas):
                duracao_j, nota_j = duracao_nota_j
                if i != j:
                    self.grafo[i].append([j, duracao_j, nota_j])

    # Conversor p/ string para debug
    def __str__(self) -> str:
        grafo_str = ""
        for vertice, arestas in enumerate(self.grafo):
            grafo_str += f"Vertice {vertice}:\n"
            for vizinho, duracao, nota in arestas:
                grafo_str += (
                    f"  - Vizinho {vizinho}, Duracao: {duracao}, Nota: {nota}\n"
                )
            grafo_str += "\n"
        return grafo_str


if __name__ == "__main__":
    print(Grafo(2, [[10, 2], [2, 3]]))
