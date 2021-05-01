from random import randint as random


def create_player():
    x = random(10, 790)
    x = (x//10) * 10
    y = random(10, 790)
    y = (y//10) * 10
    # print('player',x,y)
    tamanho = 10
    velocidade = 20
    visible = True

    return [x, y, tamanho, velocidade, visible]


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
