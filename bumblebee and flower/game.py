import pgzrun
import random
import time
WIDTH=500
HEIGHT=500
TITLE="bumblebee and flower game"
score=0
gameover=False
bee=Actor("bee")
bee.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
flower=Actor("flower")
flower.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
def draw():
    screen.blit("background",(0,0))
    if not gameover:
        bee.draw()
        flower.draw()
        screen.draw.text(f"score = {score}",(10,30))
    else:
        screen.draw.text("Your time is up!",center=(WIDTH/2,(HEIGHT/2)-10))
        screen.draw.text(f"score = {score}",center=(WIDTH/2,HEIGHT/2))
# use this to move one step at a time (not for continuous motion)
# def on_key_down(key):
#     if key==keys.UP:
#         bee.y-=10
def update():
    global score
    if keyboard.up:
        bee.y-=10
    elif keyboard.down:
        bee.y+=10
    if keyboard.left:
        bee.x-=10
    elif keyboard.right:
        bee.x+=10

    if bee.colliderect(flower):
        score=score+10
        flower.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))
def stop():
    global gameover
    gameover=True
clock.schedule(stop,15)
pgzrun.go()