from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creating the segment

snake=Snake() 

#control snake
screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")

#move snake

game_is_on= True

while game_is_on:
    screen.update()
    time.sleep(0.10)

    snake.move()
    


screen.exitonclick()
