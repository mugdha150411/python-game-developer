import pgzrun
import random
WIDTH=500
HEIGHT=500
alien=Actor("alien")
alien.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
def draw():
    screen.fill("red")
    alien.draw()
pgzrun.go()