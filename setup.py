import pygame
from functions import create_apple, create_players, melhor_player, colisao
from neural import move_players
from random import randint

pygame.init()
display = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Game com Python")

apple = []
players = []
melhorPlayer = []
rodada = 0
geracao = 1
qtd_players = 10
qtd_movimentos = 500

display_open = True
while display_open:

    pygame.time.delay(10)
    rodada += 1

    # capta acoes do botao
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            display_open = False

    # criar personagens
    if len(apple) == 0:
        apple = create_apple()
    if len(players) == 0:
        players = create_players(qtd_players, 0, 0)  # criar n players

    display.fill((0, 0, 0))  # atualiza pixels do display (limpar sombras)

    # mostrat personagens
    if apple:
        pygame.draw.circle(display, (255, 255, 255),
                           (apple[0], apple[1]), apple[2])
    if players:
        for a in players:
            pygame.draw.circle(display, (a[6][0],a[6][1],a[6][2]), (a[0], a[1]), a[2])

    # Rede Neural // mover jogadores
    players, apple = move_players(players, apple, colisao)

    # atualiza frame
    pygame.display.update()

    # verificar melhores da geração
    if rodada >= qtd_movimentos:
        pygame.time.delay(1000)
        apple = create_apple()  # nova posicao da apple

        # recebe os player com mutação em cima do melhor da geração passada
        players, qtd_players = melhor_player(players, geracao, qtd_players)

        rodada = 0
        geracao += 1


pygame.quit()
