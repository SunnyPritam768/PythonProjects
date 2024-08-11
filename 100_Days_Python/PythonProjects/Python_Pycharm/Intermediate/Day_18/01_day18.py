# Understanding of Turtle Graphics
from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("arrow")
# timmy.shape("square")
# timmy.shape("circle")
# timmy.shape("triangle")
# timmy.shape("arrow")

timmy.color("blue")
# timmy.forward(200)
# timmy.back(50)
# timmy.left(90)                # Here 90 is the angle
# timmy.forward(50)

# Task:- 1 Draw a square using Turtle Graphics
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)
timmy.right(90)
timmy.forward(200)

show = Screen()
show.exitonclick()
