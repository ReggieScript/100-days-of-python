import colorgram
from tkinter import filedialog
from tkinter import *
from re import I
from turtle import *
import numpy as np

tim = Turtle()

userpic = Tk()
userpic.filename = filedialog.askopenfilename(
    initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

colors = tuple(colorgram.extract(userpic.filename, 8))


def spirograph(rad,n_of_circles):
    tim.speed("fastest")
    for i in range(n_of_circles):
        tim.color(np.random.choice(colors).rgb)
        tim.circle(rad)
        tim.right(360/n_of_circles)

def hirst():
    tim.dot(20, np.random.choice(colors).rgb)
    tim.forward(50)


screen = Screen()
tim.penup()
screen.colormode(255)

y = -250
x = -250
tim.speed("fastest")
for i in range(10):
    tim.sety(y)
    tim.setx(x)
    for i in range(10):
        hirst()
    y += 50

# spirograph(100,100)

screen.exitonclick()
