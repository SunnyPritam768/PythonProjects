# Build a Snake Food Game
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


# Gaming Windows
show = Screen()
show.setup(600,600)
show.bgcolor("yellow")
show.title("Welcome To Snake Food Run")
show.tracer(0)

# Show Scoreboard
points = Score()

# Create Random places for food
food = Food()

# Create a snake body
my_snake = Snake()

# Set keys for the movement of the snake
show.listen()
show.onkey(my_snake.up, "Up")
show.onkey(my_snake.down, "Down")
show.onkey(my_snake.left, "Left")
show.onkey(my_snake.right, "Right")

# Move my snake mamba
game_is_on = True
while game_is_on:
    show.update()
    time.sleep(0.2)
    my_snake.move()  # Move my snake

    # Detect collision with food
    if my_snake.head.distance(food) < 15:
        food.refresh()
        my_snake.extend()
        points.runs()

    # Detect collision with Wall
    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        game_is_on = False
        points.GameOver()

    # Detect Collision with tail
    for values in my_snake.list:
        if my_snake.head == values:
            pass
        elif my_snake.head.distance(values) < 10:
            game_is_on = False
            points.GameOver()


show.exitonclick()
