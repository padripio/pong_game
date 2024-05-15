import turtle,time
from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        p=turtle.Turtle()
        self.p=p
        turtle.register_shape(name="rectangle", shape=((0, 0), (10, 0), (10, 20), (0, 20)))
        self.p.shape("rectangle")
        self.p.fillcolor("white")
        self.p.shapesize(stretch_len=5,stretch_wid=3)
    def positioning(self,x,y):
        self.p.penup()
        self.p.goto(x,y)

    #TODO move paddle
    def move_paddle_up(self):

        #self.instance_of_ball.move()
        y=self.p.ycor()
        self.p.sety(y+20)


    def move_paddle_down(self):

        #self.instance_of_ball.move()
        y = self.p.ycor()
        self.p.sety(y - 20)

