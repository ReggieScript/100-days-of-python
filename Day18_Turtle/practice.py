from re import I
from turtle import *
import numpy as np

tim = Turtle()

tim.shape("arrow")
tim.color("red")


def shapes():
    n_of_sides = 3
    while n_of_sides < 11:
        tim.color(tuple(np.random.randint(256, size=3)))
        for x in range(n_of_sides):
            tim.right(360/n_of_sides)
            tim.forward(100)
        n_of_sides += 1


def rand_walk(steps):
    tim.width(10)
    tim.speed("fastest")
    for i in range(steps):
        tim.color(tuple(np.random.randint(256, size=3)))
        tim.right(np.random.choice((0, 90, 180, 270)))
        tim.forward(30)


def spirograph(rad,n_of_circles):
    tim.speed("fastest")
    for i in range(n_of_circles):
        tim.color(tuple(np.random.randint(256, size=3)))
        tim.circle(rad)
        tim.right(360/n_of_circles)

screen = Screen()
screen.colormode(255)

# rand_walk(100)
spirograph(100,100)


def dash_line(len):
    for i in range(len):
        tim.forward(10)
        if tim.isdown():
            tim.up()
        else:
            tim.down()


screen.exitonclick()
