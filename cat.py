#!/usr/bin/python3

import turtle

turtle.shape("turtle")
turtle.shapesize(5, 5, 5)
turtle.speed(1)
turtle.color("green")

side1 = 200.1

# green triangle
turtle.penup()
turtle.setpos(-200,150)
turtle.pensize(7)
turtle.pendown()

for i in range(3):
	turtle.forward(side1)
	turtle.right(120)	

turtle.done()
