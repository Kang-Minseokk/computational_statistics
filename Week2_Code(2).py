from turtle import *

turtle = Turtle()
turtle.shape('turtle')
turtle.color('blue')
bgcolor("black")

n = 50

for x in range(n):
    turtle.circle(50)
    turtle.left(360/n)



