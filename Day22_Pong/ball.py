from turtle import Turtle
import random

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_x=random.choice((-10,-8,-6,6,8,10))
        self.ball_y=random.choice((-10,-8,-6,6,8,10))

    def move(self):
        new_x= self.xcor()+self.ball_x
        new_y=self.ycor()+self.ball_y
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ball_y=self.ball_y*-1

    def bounce_x(self):
        self.ball_x=self.ball_x*-1

    def increase_speed(self):
        if self.ball_x<25 and self.ball_x>-25:
            self.ball_x=self.ball_x*1.08
        if self.ball_y<25 and self.ball_y>-25:
            self.ball_y=self.ball_y*1.08