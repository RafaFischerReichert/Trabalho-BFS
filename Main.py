from ProblemSolver import otimizar
from typing import List

if __name__ == "__main__":
    instancia = 1
    while True:
        try:
            # Tive que utilizar IA para descobrir como receber duas inputs na mesma linha: split separa a string quando encontra um espaço e map transforma os valores em inteiros.
            atracoes, tempo_disponivel = map(
                int,
                input(
                    "Digite o numero de atracoes (1-100) e o tempo disponivel em minutos (0-600), separados por espaço. Alternativamente, digite 0 para sair: "
                ).split(),
            )

            if atracoes == 0:
                break
            if atracoes not in range(1, 101):
                raise Exception("Numero de atracoes invalido.")
            if tempo_disponivel not in range(600):
                raise Exception("Tempo invalido.")

            duracoesENotas: List[List[int]] = []
            for i in range(atracoes):

                duracao, nota = map(
                    int,
                    input(
                        f"Digite a duracao da atracao (0-600) e a nota dada (0-100), separados por espaço, para a atracao {i}: "
                    ).split(),
                )
                if duracao not in range(600):
                    raise Exception("Duracao invalida.")
                if nota not in range(100):
                    raise Exception("Nota invalida.")
                duracoesENotas.append([duracao, nota])

            melhorNota, melhorCaminho = otimizar(
                atracoes, tempo_disponivel, duracoesENotas
            )

            print(f"Instancia {instancia}")
            print(melhorNota)
            instancia += 1
        except Exception as e:
            print("Erro: ", e)
