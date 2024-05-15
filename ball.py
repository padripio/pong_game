import random
import turtle
class Ball:
    def __init__(self,r_paddle_instance,l_paddle_instance):
        self.r_paddle_instance=r_paddle_instance
        self.l_paddle_instance=l_paddle_instance
        ball = turtle.Turtle()
        self.ball = ball
        self.ball.shape("circle")
        self.ball.fillcolor("white")
        self.ball.pencolor("white")


    def start_ball(self):
        # initialise ball motion
        # fetch random angle
        self.ball.goto(0,0)
        angle1 = random.randint(300, 340)
        angle2 = random.randint(20, 60)
        angle = random.choice([angle1, angle2])
        self.ball.setheading(angle)
        self.ball.speed("slowest")
        self.ball.fd(2)

    # TODO define ball physics ,angles ,collisions ,direction
    def ball_motion(self):
        # get the heading angle
        angle = self.ball.heading()
        #for vertical walls
        angle_reflection = (360 - angle)
        self.ball.setheading(angle_reflection)
        # self.ball.fd(2)

    def move(self):

        # hits the top or bottom wall
        self.ball.fd(5)

        if self.ball.ycor() > 390 or self.ball.ycor() < -390:
            # reverse the vertical direction
            # get the heading angle
            angle = self.ball.heading()
            # for vertical walls
            angle_reflection = (360 - angle)
            self.ball.setheading(angle_reflection)

        # hits the right/left wall
        elif self.ball.xcor() > 675 or self.ball.xcor() < -675:
            # get the heading angle

            #left wall
            if self.ball.xcor() < -675:
                None
                #self.l_paddle_instance.sety(self.ball.ycor())

                #TODO detect paddle collision
                #y_paddle=self.l_paddle_instance.p.ycor()
                #y_ball=self.ball.ycor()
                #if y_paddle-50<=y_ball<=y_paddle+50:
                #    angle = self.ball.heading()
                #    angle_reflection = (angle + 90)
                #    self.ball.setheading(angle_reflection)




            elif self.ball.xcor() > 675:

                #TODO detect paddle collision
                y_paddle = self.r_paddle_instance.p.ycor()
                y_ball = self.ball.ycor()
                if y_paddle-50<=y_ball<=y_paddle+50:
                    angle = self.ball.heading()

                    angle_reflection = (angle - 90)
                    self.ball.setheading(angle_reflection)





