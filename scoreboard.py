import turtle
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color("white")
        self.penup()
        self.hideturtle()
    def increase_l(self):
        self.l_score+=1
        print(self.l_score)
    def increase_r(self):
        self.r_score+=1

    def write_scores(self):
        self.clear()

        self.goto(-200, 250)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(200, 250)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

