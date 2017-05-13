from turtle import *

shape("turtle")
speed(-1)


colors = ["red", "blue", "brown", "yellow", "grey"]


for i in range (5):
    color (colors[i])
    begin_fill()
    for n in range (2):
        forward (50)
        left(90)
        forward (100)
        left(90)

    forward (50)
    end_fill()

##
##from turtle import *
##
##shape("turtle")
##speed(-1)
##
##
##colors = ["red", "blue", "brown", "yellow", "grey"]    
##for color_stroke in colors:
##    color_stroke += 1
        
##        for j in range (i):
##            for color_stroke in color:
##                forward (100)
##                left (360/i)
##            
        

