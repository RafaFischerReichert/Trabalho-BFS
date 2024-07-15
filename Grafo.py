class Grafo:

    # Função de inicialização
    def __init__(self, number: int, direcionado: bool) -> None:
        # Iniciando uma lista vazia de tamanho predeterminado
        self.list = {i: [] for i in range(number)} 
        self.direcionado = direcionado

    # Adicionar aresta do vértice u para v
    def addAresta(self, u: int, v: int) -> None:
        self.list[u].append(v)
        if(not self.direcionado):
            self.list[v].append[u]

    # Print para debug
    def __str__(self) -> str:
        return '\n'.join(f"{node}: {neighbors}" for node, neighbors in self.list.items())
    
    # Debug
    if __name__ == "__main__":
        print(__str__)