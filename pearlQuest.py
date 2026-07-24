import pgzrun
from random import randint
WIDTH = 600
HEIGHT = 400
TITLE="Pearl Quest"

pearl=Actor("pearl")
pearl.pos=(randint(0,WIDTH),randint(0,HEIGHT))

def draw():
    global screen
    screen.fill("navy")
    pearl.draw()


def spawnner():
    pearl.pos=(randint(0,WIDTH),randint(0,HEIGHT))
clock.schedule(spawnner,1)

pgzrun.go()