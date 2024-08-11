import time
from turtle import Screen
from vertical_line import timmy, tommy

show = Screen()
show.setup(800, 600)
show.bgcolor("green")
show.title("Welcome to Ping Pong Game")
obj1 = timmy()
obj2 = tommy()

show.exitonclick()
