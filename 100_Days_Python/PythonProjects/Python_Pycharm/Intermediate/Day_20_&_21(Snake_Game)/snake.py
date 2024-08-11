from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.list = []
        self.create_snake()
        self.head = self.list[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segments(pos)

    def add_segments(self, positions):
        mamba = Turtle(shape="square")
        mamba.color("navy")
        mamba.penup()
        mamba.goto(positions)
        self.list.append(mamba)

    def extend(self):
        self.add_segments(self.list[-1].position())

    def move(self):
        for value in range(len(self.list) - 1, 0, -1):
            x_cord = self.list[value - 1].xcor()
            y_cord = self.list[value - 1].ycor()
            self.list[value].goto(x_cord, y_cord)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

