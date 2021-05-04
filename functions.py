from random import randint, uniform
import sys

def create_apple():
    x = randint(1, 199)
    y = randint(1, 199)
    tamanho = 1
    return x, y, tamanho


def create_players():
    data = []
    for i in range(1):
        temp = []
        x = randint(1, 199)
        y = randint(1, 199)
        size = 1 # pixels

        temp.append(x)
        temp.append(y)
        temp.append(size)

        #neuronios / pesos
        pesosPrimeiraCamada = []  # primeira camada
        for i in range(5):
            value = (uniform(-1, 1) for i in range(0, 3))
            pesosPrimeiraCamada.append(value)
        print(pesosPrimeiraCamada)

        # pesosCamadaOculta = []  # camada oculta
        # for i in range(4):
        #     pesosCamadaOculta.append(uniform(-1, 1) for i in range(0, 5))

        # temp.append(pesosPrimeiraCamada)
        # temp.append(pesosCamadaOculta)

        print(temp)

        data.append(temp)

    sys.exit()

    return data
