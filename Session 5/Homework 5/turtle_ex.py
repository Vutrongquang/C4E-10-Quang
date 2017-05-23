
from turtle import *

speed (-1)

##color = ["red", "yello", "pink"]
##length =[2, 3, 8]

##4.1
def draw_square(length, color):
    for i in range (4):
        fd(length)
        lt(90)

##4.2  
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

##print(draw_square)
