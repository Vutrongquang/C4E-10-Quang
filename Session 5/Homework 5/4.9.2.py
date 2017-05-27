from turtle import *

speed (-1)
color ("red")

##value = 0
##for value in range (8):

value = 0
def draw_square (value):
    for _ in range (6):
        for i in range (4):
                
            fd(value)
            left(90)
            
        value += 40
            
        penup()
        left(-90)
        fd(20)
        left(-90)
        fd(20)
        left(180)
        pendown()

draw_square(value)
            
##    value += 10
