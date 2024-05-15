import turtle
import threading

# Create a screen and turtles
s = turtle.Screen()
tom = turtle.Turtle()
tim = turtle.Turtle()

for x in [tom, tim]:
    x.shape("turtle")
    x.shapesize(2)
    x.penup()
    x.speed("slowest")

tim.sety(100)

# Function to move tom forward
def move_tom():
    for _ in range(100):
        tom.forward(10)

# Function to move tim forward
def move_tim():
    for _ in range(100):
        tim.forward(10)

# Create threads for each turtle movement function
thread1 = threading.Thread(target=move_tim)
thread2 = threading.Thread(target=move_tom)

# Start both threads
thread1.start()
thread2.start()

# Join both threads
thread1.join()
thread2.join()

# Start the main loop
turtle.mainloop()

# Make the window exit when clicked
s.exitonclick()
