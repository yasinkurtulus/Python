import random
import turtle
from tkinter import *
from turtle import Turtle,Screen,forward

import heroes
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
my_turtle=Turtle()
my_screen = Screen()

# for i in range(5):
#     my_turtle.pendown()
#     my_turtle.forward(30)
#     my_turtle.penup()
#     my_turtle.forward(30)

# for i in range(3,10):
#     angle=360/i
#     for n in range(0,i):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
my_turtle.pensize(5)
my_turtle.speed(10)
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
my_screen.colormode(255)
direction=random.randint(1,5)
for i in range(30):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_turtle.color(r,g,b)
    direction = random.randint(1, 5)
    my_turtle.forward(20)
    my_turtle.right(90*direction)


my_screen.exitonclick()
