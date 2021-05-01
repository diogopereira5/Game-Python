from random import uniform
import numpy as np


def rede_neural(player_x, player_y, fruit_x, fruit_y, pesos, pesos_oculta):
    entradas = np.array([player_x, player_y, fruit_x, fruit_y, 1])

    primeiraOculta = np.sum(entradas * pesos[0])
    segundaOculta = np.sum(entradas * pesos[1])
    terceiraOculta = np.sum(entradas * pesos[2])
    quartaOculta = np.sum(entradas * pesos[3])

    primeiraOculta = round(sigmoid(primeiraOculta), 3)
    segundaOculta = round(sigmoid(segundaOculta), 3)
    terceiraOculta = round(sigmoid(terceiraOculta), 3)
    quartaOculta = round(sigmoid(quartaOculta), 3)

    saidaOculta = np.array(
        [primeiraOculta, segundaOculta, terceiraOculta, quartaOculta])

    cima = np.sum(saidaOculta * pesos_oculta[0])
    baixo = np.sum(saidaOculta * pesos_oculta[1])
    esquerda = np.sum(saidaOculta * pesos_oculta[2])
    direita = np.sum(saidaOculta * pesos_oculta[3])    

    maior = cima
    bt = 0
    if baixo > maior:
        maior = baixo
        bt = 1
    if esquerda > maior:
        maior = esquerda
        bt = 2
    if direita > maior:
        maior = direita
        bt = 3    

    return bt, saidaOculta


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def atualizar_pesos(pesos, pesos_oculta, error, entradas, saida_oculta):

    for i in range(len(pesos_oculta)):
        pesos_oculta[i] = pesos_oculta[i] + (0.01 * saida_oculta[i] * error)

    for i in range(len(pesos)):
        pesos[i] = pesos[i] + (0.01 * entradas[i] * error)

    return pesos, pesos_oculta


def criar_pesos():
    pesos1 = np.array([uniform(-1, 1) for i in range(0, 5)])
    pesos2 = np.array([uniform(-1, 1) for i in range(0, 5)])
    pesos3 = np.array([uniform(-1, 1) for i in range(0, 5)])
    pesos4 = np.array([uniform(-1, 1) for i in range(0, 5)])
    pesos = np.array([pesos1, pesos2, pesos3, pesos4])

    peso_primeiraOculta = np.array([uniform(-1, 1) for i in range(0, 4)])
    peso_segundaOculta = np.array([uniform(-1, 1) for i in range(0, 4)])
    peso_terceiraOculta = np.array([uniform(-1, 1) for i in range(0, 4)])
    peso_quartoOculta = np.array([uniform(-1, 1) for i in range(0, 4)])
    pesos_oculta = np.array(
        [peso_primeiraOculta, peso_segundaOculta, peso_terceiraOculta, peso_quartoOculta])

    return pesos, pesos_oculta
