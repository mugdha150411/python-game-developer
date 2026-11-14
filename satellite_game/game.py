import pgzrun
import random
import time
WIDTH=500
HEIGHT=500
n=8
correct_s=0
satellites=[]
lines=[]
timer=0
start_time=time.time()
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
    screen.draw.text(f"time = {timer}",(20,20))
    for i in lines:
        screen.draw.line(i[0],i[1],"white")
def update():
    global timer
    if correct_s<n:
        timer=round(time.time()-start_time)
def on_mouse_down(pos):
    global correct_s
    global lines
    if correct_s<n:
        if satellites[correct_s].collidepoint(pos):
            if correct_s!=0:
                start=satellites[correct_s].pos
                end=satellites[correct_s-1].pos
                lines.append([start,end])
            correct_s+=1
        else:
            correct_s=0
            lines=[]
pgzrun.go()