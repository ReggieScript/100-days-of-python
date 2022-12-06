
import turtle 
from turtle import Turtle, Screen

timmy=turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color('red')

my_screen=Screen()
print(my_screen.canvheight)
timmy.speed(0)
timmy.forward(100)
my_screen.exitonclick()