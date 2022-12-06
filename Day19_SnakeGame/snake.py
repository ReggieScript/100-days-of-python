from turtle import Turtle

class Snake(object):

    def __init__(self) -> None:
        i=0
        self.segments=[]

        for segment_index in range(0,3):
            new_segment= Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(y=0, x=i)
            self.segments.append(new_segment)
            i-=20

    def move(self):
        segments=self.segments
        for seg_num in range(len(segments)-1, 0, -1):
            new_x=segments[seg_num-1].xcor()
            new_y=segments[seg_num-1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].forward(20) #20 is move distance

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

        