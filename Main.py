import pgzrun
from random import randint 

TITLE= "Good Shot"

WIDTH =500
HEIGHT =500

Bob= Actor('Bob')
message= ""

def draw():
    screen.fill(coloer=(77,77,0))
    Bob.draw()
    screen.draw.text(message, center=(400,10),fontsize=30)


def place_alien():
    Bob.x= randint(50, WIDTH-50)
    Bob.y= randint(50,HEIGHT-50)

def on_mouse_down(pos):
    global message
    if Bob.collidepoint(pos):
        message= "Good Shot"
        place_Bob()
    else:
        message= "You missed"
place_alien()
pgzrun.go()