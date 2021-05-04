from random import uniform
import numpy as np


def rede_neural(distanceX, distanceY, pesos, pesos_oculta):
    entradas = [distanceX, distanceY, 1]

    saidaOculta = []
    for i in range(len(pesos)):
        v = entradas[0] * pesos[i][0]
        v += entradas[1] * pesos[i][1]
        v += entradas[2] * pesos[i][2]
        saidaOculta.append(v)

    for i in range(len(saidaOculta)):
        if saidaOculta[i] >= 0:
            saidaOculta[i] = 1
        else:
            saidaOculta[i] = 0

    saidas = []
    for i in range(len(pesos_oculta)):
        v = saidaOculta[0] * pesos_oculta[i][0]
        v += saidaOculta[1] * pesos_oculta[i][1]
        v += saidaOculta[2] * pesos_oculta[i][2]
        v += saidaOculta[1] * pesos_oculta[i][3]
        v += saidaOculta[2] * pesos_oculta[i][4]
        saidas.append(v)

    for i in range(len(saidas)):
        saidas[i] = sigmoid(saidas[i])    

    maior = 0
    direcao = 0
    for i in range(len(saidas)):
        if saidas[i] > maior:
            maior = saidas[i]
            direcao = i

    # print(saidaOculta)

    return direcao, saidaOculta


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def atualizar_pesos(pesos, pesos_oculta, erro, entradas, saida_oculta):

    if erro > 0:

        npesos_oculta = []
        npesos = []

        for peso in pesos_oculta:
            temp = []
            for i in range(len(saida_oculta)):
                npeso = peso[i] + (uniform(-1, 1) * saida_oculta[i] * erro)
                temp.append(npeso)
            npesos_oculta.append(temp)

        for peso in pesos:
            temp = []
            for i in range(len(entradas)):
                npeso = peso[i] + (0.1 * entradas[i] * erro)
                temp.append(npeso)
            npesos.append(temp)
    else:
        npesos = pesos
        npesos_oculta = pesos_oculta

    return npesos, npesos_oculta


def criar_pesos():
    pesos1 = np.array([uniform(-1, 1) for i in range(0, 3)])
    pesos2 = np.array([uniform(-1, 1) for i in range(0, 3)])
    pesos3 = np.array([uniform(-1, 1) for i in range(0, 3)])
    pesos4 = np.array([uniform(-1, 1) for i in range(0, 3)])
    pesos5 = np.array([uniform(-1, 1) for i in range(0, 3)])
    pesos = np.array([pesos1, pesos2, pesos3, pesos4, pesos5])

    peso_primeiraOculta = np.array([uniform(-1, 1) for i in range(0, 5)])
    peso_segundaOculta = np.array([uniform(-1, 1) for i in range(0, 5)])
    peso_terceiraOculta = np.array([uniform(-1, 1) for i in range(0, 5)])
    peso_quartoOculta = np.array([uniform(-1, 1) for i in range(0, 5)])
    pesos_oculta = np.array(
        [peso_primeiraOculta, peso_segundaOculta, peso_terceiraOculta, peso_quartoOculta])

    return pesos, pesos_oculta
