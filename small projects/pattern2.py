from turtle import *

bgcolor("black")
speed(-5)
hideturtle()

for i in range(220):
    color("red")
    circle(i)
    color("white")
    circle(i*0.8)
    right(3)
    forward(3)

done()