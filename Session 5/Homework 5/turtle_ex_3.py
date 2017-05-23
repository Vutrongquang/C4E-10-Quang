from turtle import *

speed (-1)

def draw_star (x, y, length):

    penup()
    goto(x,y)
    pendown()
    for i in range (5):
        fd(length)
        lt(144)

draw_star(3,5,200)

