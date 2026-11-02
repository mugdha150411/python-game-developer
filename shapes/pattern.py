import pgzrun
import random
WIDTH=500
HEIGHT=500
def draw():
    screen.fill("light blue")
    
    screen.draw.filled_circle((100,100),53,("orange"))
    for i in range(10):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        x=random.randint(20,WIDTH-20)
        y=random.randint(HEIGHT//2+50,HEIGHT-20)
        width=random.randint(50,100)
        height=random.randint(80,200)
        box=Rect(x,y,width,height)
        box.bottomleft=x,y
        screen.draw.filled_rect(box,(r,g,b))

pgzrun.go()