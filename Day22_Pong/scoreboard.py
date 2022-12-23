from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self,alignment):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(alignment)
        self.update()

    def update(self):
        self.clear()
        self.write(self.score,align="center", font=("Courier", 80, "normal") )

    def increase_score(self):
        self.score+=1
        self.update()

    def cus_write(self,msg):
        cus=Turtle()
        cus.color("white")
        cus.hideturtle()
        cus.penup()
        cus.goto(0,0)
        cus.write(msg,align="center", font=("Courier", 85, "normal") )