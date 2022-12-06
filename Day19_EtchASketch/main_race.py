from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)

bet = screen.textinput(title="Make your bet!",
                       prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
i = -100
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=i)
    turtles.append(new_turtle)

    i += 30

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You won! {winning_color} Is the winner!")
            else:
                print(f"You lost. {winning_color} Is the winner!")
            is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
