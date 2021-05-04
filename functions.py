from random import randint, uniform
import sys

def create_apple():
    x = randint(1, 199)
    y = randint(1, 199)
    tamanho = 1
    return x, y, tamanho


def create_players(quantidade):
    data = []
    for i in range(quantidade):
        temp = []
        x = randint(1, 199)
        y = randint(1, 199)
        size = 1 # pixels

        temp.append(x) # 0
        temp.append(y) # 1
        temp.append(size) # 2

        temp.append(0) # 3 classificacao para a geracao (baseado em notas) quanto maior melhor

        #neuronios / pesos
        pesosPrimeiraCamada = []  # primeira camada
        for i in range(8):
            temp1 = []
            for j in range(3):
                value = (uniform(-1, 1))
                temp1.append(value)
            pesosPrimeiraCamada.append(temp1)
        temp.append(pesosPrimeiraCamada) # 4

        pesosCamadaOculta = []  # camada oculta
        for i in range(4):
            temp1 = []
            for j in range(8):
                value = (uniform(-1, 1))
                temp1.append(value)
            pesosCamadaOculta.append(temp1)
        temp.append(pesosCamadaOculta) # 5

        data.append(temp)

    return data
