import pygame
from functions import create_apple, create_players, mostrar_geracao
from neural import move_players

pygame.init()
display = pygame.display.set_mode((230, 230))
pygame.display.set_caption("Game com Python")

apple = []
players = []
melhorPlayer = []
rodada = 0
geracao = 1

display_open = True
while display_open:

    pygame.time.delay(100)
    rodada += 1

    # capta acoes do botao
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            display_open = False

    # criar personagens
    if len(apple) == 0:
        apple = create_apple()
    if len(players) == 0:
        players = create_players(10)  # criar n players

    display.fill((0, 0, 0))  # atualiza pixels do display (limpar sombras)

    # mostrat personagens
    if apple:
        pygame.draw.circle(display, (255, 0, 0),
                           (apple[0], apple[1]), apple[2])
    if players:
        for a in players:
            pygame.draw.circle(display, (255, 255, 255), (a[0], a[1]), a[2])

    # Rede Neural // mover jogadores
    players = move_players(players, apple)

    # atualiza frame
    pygame.display.update()

    # verificar melhores da geração
    if rodada >= 100:
        pygame.time.delay(1000)
        melhorPlayer.append(mostrar_geracao(players, geracao))
        rodada = 0
        geracao += 1

print("/n")
print("melhores pontuações por geração")
for player in melhorPlayer:
    print(player[3])

pygame.quit()
