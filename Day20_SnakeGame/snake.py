from turtle import Turtle
starting_positions = [(-20, 0), (-40, 0), (-60, 0)]


class Snake(object):

    def __init__(self) -> None:

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        segments = self.segments
        for seg_num in range(len(segments)-1, 0, -1):
            new_x = segments[seg_num-1].xcor()
            new_y = segments[seg_num-1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20)  # 20 is move distance

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]