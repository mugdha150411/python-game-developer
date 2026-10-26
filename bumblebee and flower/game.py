import pgzrun
import random
import time
WIDTH=500
HEIGHT=500
TITLE="bumblebee and flower game"
score=0
bee=Actor("bee")
bee.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
flower=Actor("flower")
flower.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(f"score = {score}",(10,30))
pgzrun.go()