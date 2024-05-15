#TODO draw the outlines
import turtle
from turtle import Turtle
def draw_outlines():
    t=turtle.Turtle()
    t.penup()
    #middle divider
    t.pencolor("white")
    t.goto(0,-400)
    t.setheading(90)
    y=-400
    while y<400:
        t.speed("fastest")
        t.pendown()
        t.fd(30)
        t.penup()
        t.fd(20)
        t.pendown()
        y=t.ycor()
    t.penup()

    #player walls /currently invisible

    t.goto(-700,-400)
    t.setheading(90)
    y=-400
    while y<450:
        t.penup()
        t.fd(30)
        #t.penup()
        t.fd(15)
        t.pendown()
        y=t.ycor()
    t.penup()
    t.goto(700,-400)
    t.setheading(90)
    y=-400
    while y<400:
        t.penup()
        t.fd(30)
        #t.penup()
        t.fd(15)
        t.pendown()
        y=t.ycor()


    #TODO draw the walls
    #upper wall
    t.penup()
    t.goto(-700,410)
    x=-700
    t.setheading(0)
    t.pensize(8)
    t.pendown()
    while x<700:
        t.fd(10)
        x=t.xcor()

    #lower wall
    t.penup()
    t.goto(-700, -410)
    x = -700
    t.setheading(0)

    t.pendown()
    while x < 700:

        t.fd(10)
        x=t.xcor()


    t.pencolor("black")
    t.fd(50)