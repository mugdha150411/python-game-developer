import pgzrun
import random
WIDTH=500
HEIGHT=500
def draw():
    screen.fill("black")
    side=50

    for i in range(10):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        box=Rect(0,0,side,side)
        box.center=(WIDTH/2,HEIGHT/2)
        screen.draw.rect(box,(r,g,b))
        side=side+30
pgzrun.go()