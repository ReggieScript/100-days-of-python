import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross The Road")
screen.tracer(0)
screen.bgcolor("Black")

player = Player()
cars = [CarManager()]
score=Scoreboard()


game_is_on = True

screen.listen()
screen.onkeypress(player.move, "Up")
i = 0
fast=1
x=6 #variable for how many loops it needs to have to create a car object

while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move(fast)
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False
        if car.xcor() < -340:
            cars.remove(car) #This line prevents from creating too many car objects and improves performance of the game
    if i == x:
        cars.append(CarManager())
        i = 0
    if player.ycor() >= 280:
        player.restart()
        if score.level ==6:
            score.win()
            game_is_on=False
        score.increase_level()
        fast+=0.5
        x-=1 # this will probably create a bug when reaching level 6, which is why I'm stopping it at level 5

    i += 1

screen.exitonclick()