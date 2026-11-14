import pgzrun
import random
import time
HEIGHT=350
WIDTH=500
TITLE="Monkey and the bananas game"
score=0
GAMEOVER=False
monkey=Actor("monkey")
monkey.pos=(WIDTH/2,HEIGHT-30)
bananas=[]
coconuts=[]
for i in range(10):
    banana=Actor("banana")
    banana.pos=(random.randint(20,WIDTH-20),0)
    bananas.append(banana)
for i in range(5):
    coconut=Actor("coconut")
    coconut.pos=(random.randint(20,WIDTH-20),0)
    coconuts.append(coconut)
def draw():
    screen.blit("bg",(0,0))
    monkey.draw()
    screen.draw.text(f"score = {score}",(10,30))
def update():
    global score
    if keyboard.left:
        monkey.x-=10
    elif keyboard.right:
        monkey.x+=10
pgzrun.go()