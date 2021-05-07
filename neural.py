import numpy as np
from random import randint, uniform
import sys


def move_players(players, apple, colisao):
    for player in players:
        # pega posicao mais indicada a seguir pela rede neural
        direcao, en1, en2 = rede_neural(player, apple)

        # pontuacao
        distanceX = apple[0] - player[0]
        distanceY = apple[1] - player[1]
        if distanceX == 0 and distanceY == 0:
            player[3] += 100  # recebe nota 100 por pegar a fruta

        # ++++++++++++++++++++++++++++++++++++++++++++++++++
        # move player para a nova posicao na matrix
        if direcao == 0:  # UP
            if player[1] >= 10:
                player[1] -= 1

        if direcao == 1:  # RIGHT
            if player[0] <= 190:
                player[0] += 1

        if direcao == 2:  # DOWN
            if player[1] <= 190:
                player[1] += 1

        if direcao == 3:  # LEFT
            if player[0] >= 10:
                player[0] -= 1

        NdistanceX = apple[0] - player[0]
        NdistanceY = apple[1] - player[1]

        # colisao de player com apple
        apple = colisao(players, apple)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++
        # pontuacao
        if NdistanceX < distanceX:
            player[3] += 1  # recebe nota 1 por está mais PROXIMO da apple
        if NdistanceX > distanceX:
            player[3] -= 1  # recebe nota -1 por está mais LONGE da apple
            player[4] = atualiza_peso_erro(player[4], 8, 3, 1, en1)
            player[5] = atualiza_peso_erro(player[5], 4, 8, 1, en2)

        if NdistanceY < distanceY:
            player[3] += 1  # recebe nota 1 por está mais PROXIMO da apple
        if NdistanceY > distanceY:
            player[3] -= 1  # recebe nota -1 por está mais LONGE da apple
            player[4] = atualiza_peso_erro(player[4], 8, 3, 1, en1)
            player[5] = atualiza_peso_erro(player[5], 4, 8, 1, en2)

        # player nao andar
        if NdistanceX == distanceX and NdistanceY == distanceY:
            player[3] -= 1  # recebe nota -1 por está mais LONGE da apple
            player[4] = atualiza_peso_erro(player[4], 8, 3, 1, en1)
            player[5] = atualiza_peso_erro(player[5], 4, 8, 1, en2)


    return players, apple


def rede_neural(player, apple):
    distanceX = apple[0] - player[0]
    distanceY = apple[1] - player[1]
    entradas = np.array([distanceX, distanceY, 1])

    # entrada primeira camada oculta
    pesosPrimeiraCamada = np.array(player[4])
    EntradaPrimeiraCamadaOculta = []

    for peso in pesosPrimeiraCamada:
        v = np.sum(peso * entradas)
        # v = 1
        if v >= 1:
            v = 1
        else:
            v = 0
        EntradaPrimeiraCamadaOculta.append(v)

    # entrada primeira camada oculta
    pesosPrimeiraCamadaOculta = np.array(player[5])
    saida = []

    for peso in pesosPrimeiraCamadaOculta:
        v = np.sum(peso * EntradaPrimeiraCamadaOculta)
        v = sigmoid(v)
        saida.append(v)

    # verifica o valor com maior probabilidade
    maior = 0
    direcao = 0
    for i in range(len(saida)):
        if saida[i] > maior:
            maior = saida[i]
            direcao = i

    return direcao, entradas, EntradaPrimeiraCamadaOculta


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def atualiza_peso(peso, value1, value2):
    data = []
    size = len(peso) - 1
    if size < 0:
        size = 0
    v = int(randint(0, size))
    for i in range(value1):
        temp1 = []
        for j in range(value2):
            if j == v:
                value = (uniform(-1, 1))
                temp1.append(value)
            else:
                temp1.append(peso[i][j])
        data.append(temp1)
    return data


def atualiza_peso_erro(peso, value1, value2, erro, entrada):
    data = []
    for i in range(value1):
        temp1 = []
        for j in range(value2):
            value = peso[i][j] + (0.1 * entrada[j] * erro)
            temp1.append(value)
        data.append(temp1)
    return data
