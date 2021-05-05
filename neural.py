import numpy as np
import sys

def move_players(players, apple):

    for player in players:
        direcao = rede_neural(player, apple) # pega posicao mais indicada a seguir pela rede neural

        #pontuacao
        distanceX = apple[0] - player[0]
        distanceY = apple[1] - player[1]
        if (distanceX + distanceY) == 0:
            player[3] += 100 #recebe nota 100 por pegar a fruta

        #++++++++++++++++++++++++++++++++++++++++++++++++++
        #move player para a nova posicao na matrix
        if direcao == 0: # UP
            if player[1] >= 10:
                player[1] -= 1

        if direcao == 1: # RIGHT
            if player[0] <= 190:
                player[0] += 1

        if direcao == 2: # DOWN
            if player[1] <= 190:
                player[1] += 1

        if direcao == 3: #LEFT
            if player[0] >= 10:
                player[0] -= 1

        NdistanceX = apple[0] - player[0]
        NdistanceY = apple[1] - player[1]

        #++++++++++++++++++++++++++++++++++++++++++++++++++
        #pontuacao
        if NdistanceX < distanceX:
            player[3] += 1 #recebe nota 1 por está mais PROXIMO da apple
        elif NdistanceX >= distanceX:
            player[3] -= 1 #recebe nota -1 por está mais LONGE da apple

        if NdistanceY < distanceY:
            player[3] += 1 #recebe nota 1 por está mais PROXIMO da apple
        elif NdistanceY >= distanceY:
            player[3] -= 1 #recebe nota -1 por está mais LONGE da apple

    return players


def rede_neural(player, apple):
    distanceX = apple[0] - player[0]
    distanceY = apple[1] - player[1]
    entradas = np.array([distanceX, distanceY, 1])

    # entrada primeira camada oculta
    pesosPrimeiraCamada = np.array(player[4])
    EntradaPrimeiraCamadaOculta = []

    for peso in pesosPrimeiraCamada:
        v = np.sum(peso * entradas)
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

    #verifica o valor com maior probabilidade 
    maior = 0
    direcao = 0
    for i in range(len(saida)):
        if saida[i] > maior:
            maior = saida[i]
            direcao = i

    return direcao


def sigmoid(x):
    return 1 / (1 + np.exp(-x))
