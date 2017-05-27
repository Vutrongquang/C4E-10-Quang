from turtle import *

speed(-1)

color("red")

n = 0
size = 0

def draw_equitriangle(n, size):
    for i in range (n):
        fd(size)
        left(360/n)

draw_equitriangle(3,100)
