from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#tried to add pog sound when hit by paddle, but it slowed the program down, will try with threading in the future

# from playsound import playsound

global game_is_on
# variables de movimiento de la pelota

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG: The Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
r_score = Scoreboard((100, 200))

l_paddle = Paddle((-350, 0))
l_score = Scoreboard((-100, 200))
ball = Ball()


screen.listen()
# right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

#left paddle

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()

    ball.move()

# Posibilidad de bug si la pelota brinca de otras maneras

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detectar la colision con el paddle

    if ball.xcor() > 340 and r_paddle.distance(ball) < 50:
        ball.bounce_x()
        r_score.increase_score()
        ball.increase_speed()
        # playsound("Day22_Pong\pong_sound.mp3",block=False)

    if ball.xcor() < -340 and l_paddle.distance(ball) < 50:
        ball.bounce_x()
        l_score.increase_score()
        ball.increase_speed()
        # playsound("Day22_Pong\pong_sound.mp3",block=False)

# Que pasa si la pelota se pasa de los paddles

    if ball.xcor() > 380:
        ball.bounce_x()
        l_score.increase_score()

    if ball.xcor() < -380:
        ball.bounce_x()
        r_score.increase_score()


    if r_score.score == 11:
        r_score.cus_write("RIGHT WINS!")
        game_is_on=False
    if l_score.score ==11:
        l_score.cus_write("LEFT WINS!")
        game_is_on=False

    time.sleep(.05)


screen.exitonclick()
