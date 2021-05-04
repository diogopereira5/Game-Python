from random import randint as random

def create_fruit():
    x = random(10, 790)
    x = (x//10) * 10
    y = random(10, 790)
    y = (y//10) * 10
    # print('fruit',x,y)
    tamanho = 10
    visible = True

    return [x,y,tamanho,visible]