from turtle import *

speed(-1)
color ("red")

n =0
size = 0

def draw_poly(n, size):
    for i in range (n):
        forward (size)
        left (360/n)

draw_poly(10, 100)

# khong hieu tess la gi va tai sao lai cho tess vao
