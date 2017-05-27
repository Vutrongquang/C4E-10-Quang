from turtle import *

speed (-1)
color ("red")

def draw_square():
    for y in range (10):
        for _ in range (4):
            for i in range (4):
                fd(50)
                left(90)
            left(90)
        left(20)

draw_square()

