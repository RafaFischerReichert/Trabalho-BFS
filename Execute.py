# from Grafo.py import Grafo
from time import sleep
import Grafo

badNumber: str = "Valor inválido."

def execute() -> None:
    while(True):
        try:
            # Usei AI para entender como juntar duas inputs. A função map converte strings em inteiros, e split separa as strings.
            rides, time = map(int, input("Digite o número de atrações (0-100) e o tempo disponível em minutos (0-600), separados por espaço: ").split())

            # Condição de parada
            if(rides == 0):
                break

            # Limites dos valores
            if(rides not in range(100) or time not in range(600)):
                raise Exception (badNumber)

            # Inicializando lista
            list_of_rides = []

            for n in range(rides):
                duration, rating = map(int, input(f"Digite a duração da atração {n + 1} em minutos (0-600) e sua nota (0-100), separados por espaço:").split())

                # Limites dos valores
                if (duration not in range(600) or rating not in range(100)):
                    raise Exception (badNumber)
                
                list_of_rides.append((duration, rating))

            # Debug
            if __name__ == "__main__":
                print(list_of_rides)


        except Exception as e:
            print("Erro: ", e)
            sleep(5)
            break