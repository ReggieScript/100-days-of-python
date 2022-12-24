from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("Day20_SnakeGame\highscore.txt",mode="r") as file:
            self.high_score=int(file.read())
        self.score=0
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center", font=("Arial", 24, "normal") )

    def increase_score(self):
        self.score+=1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center", font=("Arial", 24, "normal") )

    def reset(self):
        if self.score > self.high_score:
            with open("Day20_SnakeGame\highscore.txt",mode="w") as file:
                file.write(str(self.score))
            self.high_score=self.score
        self.score=0
        self.update()

    def game_over(self):
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial",50, "normal"))
