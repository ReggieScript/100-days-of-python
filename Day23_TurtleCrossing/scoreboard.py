from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level=1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.write(f"Level: {self.level}",align="center", font=FONT)
        
    def increase_level(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}",align="center", font=FONT)

    def game_over(self):
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=FONT)

    def win(self):
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write("YOU WIN!", align="center",font=FONT)
