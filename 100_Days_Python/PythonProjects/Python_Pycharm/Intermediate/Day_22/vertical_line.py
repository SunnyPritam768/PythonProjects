from turtle import Turtle
import time

timmy = Turtle()
tommy = Turtle()
gap = 20
timmy.shape("triangle")
timmy.left(90)
tommy.right(90)

play = True
while play:
    time.sleep(1)
    for value in range(1, 11):
        timmy.forward(gap)
        timmy.penup()
        timmy.forward(gap)
        timmy.pendown()

    for value in range(1, 11):
        tommy.forward(gap)
        tommy.penup()
        tommy.forward(gap)
        tommy.pendown()
    play = False
