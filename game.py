import pygame
from player import create_player, move_player
from fruit import create_fruit

pygame.init()

players = []
fruits = []

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Game com Python")
display.fill((190, 190, 190))

new_player = False
display_open = True
while display_open:

    pygame.time.delay(50)

    # capta acoes do botao
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            display_open = False

        # novo player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(players) < 1:
                    players.append(create_player())

    # eventos do teclado
    comandos = pygame.key.get_pressed()
    if len(players) != 0:  # se nao houver player, nao tera acao de botao
        move_player(pygame, comandos, players[0])

    display.fill((190, 190, 190))  # atualiza pixels do display

    # mostrar fruta
    if len(fruits) == 0:
        fruits.append(create_fruit())

    if fruits:
        for i in fruits:
            if i[3]:
                pygame.draw.circle(display, (255, 0, 0), (i[0], i[1]), i[2])

    # mostrar novos players no display
    if players:
        for i in players:
            if i[4]:
                pygame.draw.circle(display, (10, 10, 255), (i[0], i[1]), i[2])

    pygame.display.flip()

    # atualizar sombra do objeto
    pygame.display.update()

pygame.quit()
