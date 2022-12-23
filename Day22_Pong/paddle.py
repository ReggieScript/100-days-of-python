from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() >= 250: #limits so that the paddle will not go off the screen
            pass
        else:
            new_y = self.ycor()+50
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() <= -250: #limits so that the paddle will not go off the screen
            pass
        else:
            new_y = self.ycor()-50
            self.goto(self.xcor(), new_y)
