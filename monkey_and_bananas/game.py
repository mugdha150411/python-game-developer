import pgzrun
import random
import time
HEIGHT=350
WIDTH=500
TITLE="Monkey and the bananas game"
score=0
gameover=False
monkey=Actor("monkey")
monkey.pos=(WIDTH/2,HEIGHT-30)
banana=Actor("banana")
coconut=Actor("coconut")
def draw():
    screen.blit("bg",(0,0))
    monkey.draw()
    screen.draw.text(f"score = {score}",(10,30))
    if not gameover:
        banana.draw()
        banana.pos=(random.randint(20,WIDTH-20),0)
        coconut.draw()
        coconut.pos=(random.randint(20,WIDTH-20),0)
    else:
        screen.draw.text("Your time is up!",center=(WIDTH/2,(HEIGHT/2)-15))
        screen.draw.text(f"score = {score}",center=(WIDTH/2,HEIGHT/2))
def update():
    global bananas
    global coconuts
    global gameover
    global score
    if keyboard.left:
        monkey.x-=10
    elif keyboard.right:
        monkey.x+=10
    if not gameover:
        banana.y+=10
        coconut.y+=10
    if monkey.collidepoint(banana):
        score+=10
        banana.pos=(random.randint(20,WIDTH-20),0)
    elif monkey.collidepoint(coconut):
        score+=0
        coconut.pos(random.randint(20,WIDTH-20),0)
def stop():
    global gameover
    gameover=True
clock.schedule(stop,20)
pgzrun.go()