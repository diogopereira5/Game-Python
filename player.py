from random import randint as random

def create_player():
    x = random(0, 800)
    y = random(0, 800)
    tamanho = 10
    velocidade = 15
    visible = True

    return [x,y,tamanho,velocidade,visible]
    
def move_player(pygame,comandos,position):
    if comandos[pygame.K_UP]:
        if position[1] >= 0:
            position[1] -= position[3]
    if comandos[pygame.K_DOWN]:
        if position[1] <= 800:
            position[1] += position[3]
    if comandos[pygame.K_LEFT]:
        if position[0] >= 0:
            position[0] -= position[3]
    if comandos[pygame.K_RIGHT]:
        if position[0] <= 800:
            position[0] += position[3]