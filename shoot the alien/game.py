import pgzrun
import random
WIDTH=500
HEIGHT=500
alien=Actor("alien")
alien.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
msg=""
def draw():
    screen.fill("red")
    alien.draw()
    screen.draw.text(msg,center=(WIDTH/2,45),color="black",fontsize=30)

def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
         msg="you found the alien"
         alien.pos=random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50)
    else:
        msg="try again"
    #alien.pos=pos
pgzrun.go()