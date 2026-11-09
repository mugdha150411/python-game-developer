import pgzrun
import random
import time
WIDTH=500
HEIGHT=500
n=8
correct_s=0
satellites=[]
for i in range(n):
    satellite=Actor("satellite")
    satellite.pos=(random.randint(20,WIDTH-20),random.randint(20,HEIGHT-20))
    satellites.append(satellite)
def draw():
    screen.blit("bg_night_sky",(0,0))
    num=1
    for i in satellites:
        i.draw()
        screen.draw.text(str(num),i.midbottom)
        num+=1
def on_mouse_down(pos):
    if satellites[correct_s].collidepoint(pos):
pgzrun.go()