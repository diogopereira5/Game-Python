from random import randint, uniform
import numpy as np
import sys
from neural import atualiza_peso


def create_apple():
    x = (randint(10, 191) // 10) * 10
    y = (randint(10, 191) // 10) * 10
    tamanho = 5
    return x, y, tamanho


def create_players(quantidade, peso1, peso2):
    data = []
    for i in range(quantidade):
        temp = []
        x = (randint(10, 191) // 10) * 10
        y = (randint(10, 191) // 10) * 10
        size = 5  # pixels

        temp.append(x)  # 0
        temp.append(y)  # 1
        temp.append(size)  # 2

        # 3 classificacao para a geracao (baseado em notas) quanto maior melhor
        temp.append(0)

        #neuronios / pesos
        pesosPrimeiraCamada = []  # primeira camada
        if peso1 == 0:
            for i in range(8):
                temp1 = []
                for j in range(3):
                    value = (uniform(-1, 1))
                    temp1.append(value)
                pesosPrimeiraCamada.append(temp1)
        else:  # se houver valor pre definidor, preencher aqui no individuo
            pesosPrimeiraCamada = atualiza_peso(peso1, 8, 3)

        temp.append(pesosPrimeiraCamada)  # 4

        pesosCamadaOculta = []  # camada oculta
        if peso2 == 0:
            for i in range(4):
                temp1 = []
                for j in range(8):
                    value = (uniform(-1, 1))
                    temp1.append(value)
                pesosCamadaOculta.append(temp1)
        else:  # se houver valor pre definidor, preencher aqui no individuo
            pesosCamadaOculta = atualiza_peso(peso2, 4, 8)

        temp.append(pesosCamadaOculta)  # 5

        # definir cor
        cor = []
        r = randint(0, 255)
        cor.append(r)
        g = randint(0, 255)
        cor.append(g)
        b = randint(0, 255)
        cor.append(b)

        temp.append(cor)  # 6

        data.append(temp)

    return data


def melhor_player(players, geracao, qtd_players):

    print("______________________")
    print("Teste com "+str(geracao)+"ª geração")
    # n = 1
    # for player in players:
    #     print("Player: "+str(n)+" - Pontuação = "+str(player[3]))
    #     n += 1

    # verificar o melhor indíviduo para mutação
    tempMelhor = 0
    position = 0
    n = 0
    for player in players:
        if tempMelhor != 0:
            if player[3] > tempMelhor:
                tempMelhor = player[3]
                position = n
        else:
            tempMelhor = player[3]
            position = n
        n += 1

    print("Melhor Player: N°", str(position+1),
          str(players[position][3]), "Pts")

    # qtd_players -= 1

    # if qtd_players <= 0:
    #     qtd_players = 1

    # mutação nos players
    peso1 = players[position][4]
    peso2 = players[position][5]
    players = create_players(qtd_players, peso1, peso2)

    qtd_players -= 1

    if qtd_players < 1:
        qtd_players = 1

    return players, qtd_players


def colisao(players, apple):

    for player in players:
        # if (player[0]) == apple[0] and (player[1]) == apple[1]:
        #     print("pegou!")
        #     return create_apple()
        if apple[0] >= (player[0] - (player[2])) and apple[0] <= (player[0] + (player[2])) and apple[1] >= (player[1] - (player[2])) and apple[1] <= (player[1] + (player[2])):
            return create_apple()

    return apple
