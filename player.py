from random import randint as random
from ia import rede_neural


def create_player():

    data = []
    for i in range(10):

        x = random(10, 790)
        x = (x//10) * 10
        y = random(10, 790)
        y = (y//10) * 10
        # print('player',x,y)
        tamanho = 10
        velocidade = 20
        visible = True
        corR = random(0, 256)
        corG = random(0, 256)
        corB = random(0, 256)

        data.append([x, y, tamanho, velocidade, visible, [corR, corG, corB]])

    return data


def move_player(pygame, comandos, position):
    if comandos[pygame.K_UP]:
        if position[1] >= (0 + position[2]):
            position[1] -= position[3]
    if comandos[pygame.K_DOWN]:
        if position[1] <= (800 - position[2]):
            position[1] += position[3]
    if comandos[pygame.K_LEFT]:
        if position[0] >= (0 + position[2]):
            position[0] -= position[3]
    if comandos[pygame.K_RIGHT]:
        if position[0] <= (800 + position[2]):
            position[0] += position[3]


def move_player_ia(distanceX, distanceY, position, pesos, pesos_oculta):
    direcao, saida_oculta = rede_neural(
        distanceX, distanceY, pesos, pesos_oculta)

    if direcao == 0:
        if position[1] >= 20:
            position[1] -= position[3]
    if direcao == 1:
        if position[1] <= 780:
            position[1] += position[3]
    if direcao == 2:
        if position[0] >= 20:
            position[0] -= position[3]
    if direcao == 3:
        if position[0] <= 780:
            position[0] += position[3]

    return position[0], position[1], saida_oculta
