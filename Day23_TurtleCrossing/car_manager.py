from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
move_distance = 10

class CarManager(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        # With this randint we generate random numbers to fill the y axis, only evrey 20 so that the cars dont overlap
        self.goto(320, random.randint(-12, 12)*20)

    def move(self,fast):
        new_x = self.xcor()-move_distance*fast
        self.goto(new_x, self.ycor())

