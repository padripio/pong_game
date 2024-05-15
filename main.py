import turtle
import random
from turtle import Turtle , Screen
from paddles import Paddle
from outline import draw_outlines
from ball import Ball
from scoreboard import Scoreboard
#TODO create a screen
s=turtle.Screen()
s.bgcolor("black")

#TODO define boundaries
s.setup(width=1400 ,height=800)




#TODO scoreboard

#TODO user motion events
class score:
    pass


def main():
    turtle.listen()
    s.tracer(0)


    draw_outlines()
    l_paddle = Paddle()
    r_paddle = Paddle()
    pong = Ball(r_paddle,l_paddle)


    s.update()



    # TODO define motion limits

    paddle1_lower = [-350, -350]
    paddle2_lower = [350, -350]
    paddle1_upper = [-720, 400]
    paddle2_upper = [700, 400]

    s.tracer(0)


    l_paddle.positioning(paddle1_lower[0], paddle1_lower[1])

    r_paddle.positioning(paddle2_lower[0], paddle2_lower[1])
    s.update()

    # TODO initialise heading
    for _ in [l_paddle, r_paddle]:
        _.p.setheading(90)

    # todo initialise motion
    paddle_list = [l_paddle]
    #d = 10

    pong.ball.penup()
    pong.start_ball()
    pace=0
    pong.ball.speed("fastest")

    # TODO up and down paddle motion
    def move_up():
        if r_paddle.p.ycor()<=700:
            r_paddle.move_paddle_up()
        else:
            r_paddle.p.sety(700)

    def move_down():
        if r_paddle.p.ycor()>=-700:
            r_paddle.move_paddle_down()
        else:
            r_paddle.p.sety(-700)

    turtle.onkey(fun=move_up, key="Up")
    turtle.onkey(fun=move_down, key="Down")

    def update_game():

        scores = Scoreboard()
        #scores.write_scores()


        pong.move()
        if pong.ball.xcor()<-680:
            l_paddle.p.sety(pong.ball.ycor())
        if pong.ball.xcor() > 720:
            print("yess")
            scores.increase_l()
            pong.start_ball()
        elif pong.ball.xcor()<-720:
            scores.increase_r()
            pong.start_ball()
        scores.write_scores()
        #scores.clear()


        s.update()

        s.ontimer(update_game, 10)  # Update every 10 milliseconds
    update_game()


            # x.p.setheading(270)



if __name__=="__main__":
    main()
turtle.mainloop()



#def update_game():
#    pong.move()  # Update ball position
#    screen.update()  # Update screen
#
#    # Check for collisions with walls
#    if pong.ball.ycor() >= 390 or pong.ball.ycor() <= -390:
#        pong.ball.dy *= -1
#    if pong.ball.xcor() >= 690 or pong.ball.xcor() <= -690:
#        pong.ball.dx *= -1
#
#    # Schedule the next update
#    screen.ontimer(update_game, 10)  # Update every 10 milliseconds
#
#    # Start the game loop
#
#
#update_game()
