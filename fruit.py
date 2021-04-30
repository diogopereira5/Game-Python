from random import randint as random

def create_fruit():
    x = random(0, 800)
    y = random(0, 800)
    tamanho = 5
    visible = True

    return [x,y,tamanho,visible]