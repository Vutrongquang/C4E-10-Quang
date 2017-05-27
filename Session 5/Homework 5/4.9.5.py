from turtle import *

speed (-1)
color ("red")

value = 0
n = 0
angle = 0
def draw_square(value, n, angle):

    for i in range (n):
        for i in range (1):
            fd(value)
            left(90)
            
            fd(value)
            left(90)
            
            fd(value + 10)
            left(90)
            
            fd(value + 10)
            left(90)

            
        value += 20
        
draw_square(4, 4, 0)
