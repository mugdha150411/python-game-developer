import pgzrun
WIDTH=500
HEIGHT=500
lines=[]
FILE_NAME="questions.txt"
marqueebox=Rect(0,0,500,30)
def draw():
    screen.fill("light blue")
    screen.draw.filled_rect(marqueebox,"black")
def read_file():
    global lines
    f=open(FILE_NAME,"r")
    lines=f.read().split("\n")
    f.close()
    print(lines)
read_file()
pgzrun.go()