from turtle import Turtle, Screen
import random

# Draw a Spirograph using Turtle Graphics
timmy = Turtle()
timmy.speed("fastest")
radius = 100
shift = 10
turns = 37

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Set the colormode to 255
Screen().colormode(255)

for i in range(turns):
    timmy.color(random_color())
    timmy.circle(radius)
    timmy.left(shift)

# How to show on Screen
show = Screen()
show.exitonclick()
