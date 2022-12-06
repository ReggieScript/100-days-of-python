from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

def move_foward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clockwise():
    tim.right(10)

def counter_clockwise():
    tim.left(10)


screen.listen()
screen.onkey(key="w", fun=move_foward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.exitonclick()