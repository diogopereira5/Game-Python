import pygame
from player import create_player, move_player, move_player_ia
from fruit import create_fruit
from ia import rede_neural, criar_pesos, atualizar_pesos
import numpy as np
from random import uniform

pygame.init()

players = []
fruits = []
pesos,pesos_oculta = criar_pesos()
error = 0
rodada = 0

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Game com Python")
display.fill((190, 190, 190))

new_player = False
display_open = True
while display_open:

    pygame.time.delay(50)
    saida_oculta = []    
    rodada += 1
    distance = 0

    # capta acoes do botao
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            display_open = False

        # novo player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(players) < 1:
                    players.append(create_player())
            if event.key == pygame.K_LSHIFT:
                rede_neural(players[0][0], players[0][1],
                            fruits[0][0], fruits[0][1], pesos, pesos_oculta)

    # eventos do teclado
    comandos = pygame.key.get_pressed()
    if len(players) != 0:  # se nao houver player, nao tera acao de botao
        move_player(pygame, comandos, players[0])

    # i.a jogando aqui
    if len(players) != 0:  # se nao houver player, nao tera acao de botao
        players[0][0], players[0][1], saida_oculta = move_player_ia(players[0][0], players[0][1],
                       fruits[0][0], fruits[0][1], players[0], pesos, pesos_oculta)        
        distance = abs(players[0][0] - fruits[0][0])
        distance = error + (abs(players[0][1] - fruits[0][1]))

    # colisao do player + fruta
    if players and fruits:
        if fruits[0][0] >= (players[0][0] - (players[0][2])) and fruits[0][0] <= (players[0][0] + (players[0][2])) and fruits[0][1] >= (players[0][1] - (players[0][2])) and fruits[0][1] <= (players[0][1] + (players[0][2])):
            fruits[0] = create_fruit()  # nova fruta
            players[0][2] += fruits[0][2]  # aumenta tamnaho player
            players[0][3] -= 1  # velocide do player
            if players[0][3] <= 1:
                players[0][3] = 1
        else:
            new_distance = abs(players[0][0] - fruits[0][0])
            new_distance = error + (abs(players[0][1] - fruits[0][1]))
            if distance < new_distance:
                error = new_distance / 100
            
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

    if rodada >= 20:
        error = uniform(-1,1)

    #calcular erro
    if players and fruits:
        entradas = np.array([players[0][0], players[0][1],fruits[0][0], fruits[0][1], players[0], 1])
        pesos, pesos_oculta = atualizar_pesos(pesos,pesos_oculta,error,entradas,saida_oculta)

pygame.quit()
