# -*- coding:utf-8 -*-
import turtle

turtle.pensize(2)
turtle.bgcolor("black")
colors = ['red', 'yellow', 'purple', 'blue']
turtle.speed(10)
for x in range(400):
    turtle.forward(1.1*x)
    turtle.color(colors[x % 4])
    turtle.left(91)
turtle.tracer(True)
turtle.done()
