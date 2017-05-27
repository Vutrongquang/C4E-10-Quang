from turtle import *

speed (-1)
color ("red", "blue")

def draw_square():
    for _ in range (8):
        begin_fill()
        for i in range (4):

            fd(50)
            lt(90)

        penup()
        fd (100)
        pendown()

        end_fill()

draw_square()
