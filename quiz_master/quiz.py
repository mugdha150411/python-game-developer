import pgzrun
WIDTH=500
HEIGHT=390
lines=[]
FILE_NAME="questions.txt"
marqueebox=Rect(0,0,500,30)
questionbox=Rect(10,40,350,100)
timerbox=Rect(370,40,120,100)
op_box1=Rect(10,150,170,100)
op_box2=Rect(190,150,170,100)
op_box3=Rect(10,260,170,100)
op_box4=Rect(190,260,170,100)
option_boxes=[op_box1,op_box2,op_box3,op_box4]
skipbox=Rect(370,150,120,210)
total_qs=0
current_qs=0
qs_time=10
def draw():
    screen.fill("light blue")
    screen.draw.filled_rect(marqueebox,"black")
    screen.draw.filled_rect(questionbox,"dark green")
    screen.draw.filled_rect(timerbox,"purple")
    for i in option_boxes:
        screen.draw.filled_rect(i,"black")
    screen.draw.filled_rect(skipbox,"dark blue")

    screen.draw.textbox(f"WELCOME TO QUIZ MASTER. THIS IS QUESTION {current_qs} OF {total_qs}",marqueebox,color="white")
    screen.draw.textbox("SKIP",skipbox,color="white",angle=45)
    screen.draw.textbox(str(qs_time),timerbox,color="yellow")
def update():
    marqueebox.x=marqueebox.x-2
    if marqueebox.right<=0:
        marqueebox.left=WIDTH

def read_file():
    global lines,total_qs
    f=open(FILE_NAME,"r")
    lines=f.read().split("\n")
    f.close()
    print(lines)
    total_qs=len(lines)

read_file()
pgzrun.go()