import turtle,threading
from turtle import  Turtle,Screen
s=turtle.Screen()
tom=turtle.Turtle()
tim=turtle.Turtle()

for x in [tom,tim]:
    x.shape("turtle")
    x.shapesize(2)
    x.penup()
    x.speed("slowest")

tim.sety(100)




#TODO get tom and tim to move forward by threading
def move_tom():
    for i in range (100):
        tom.forward( 10)

def move_tim():
    for i in range (100):
        tim.forward( 10)



thread1=threading.Thread(target=move_tim)
thread2=threading.Thread(target=move_tom)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
#turtle.mainloop()
while True:
    if s._root is None or s._root.quit or s._root.destroyed:
        break

# Exit gracefully
s.bye()


#s.exitonclick()