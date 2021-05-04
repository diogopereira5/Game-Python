import numpy as np

def move_players(players,apple):

    for player in players:
        a, b = rede_neural(player,apple)

    return players


def rede_neural(player,apple):
    distanceX = apple[0] - player[0]
    distanceY = apple[1] - player[1]

    return 0, 0
