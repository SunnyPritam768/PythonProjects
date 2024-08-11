from turtle import Turtle
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score is: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def GameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -40)
        self.write(f"Your score is: {self.score}", align="center", font=("Arial", 24, "normal"))

    def runs(self):
        self.score += 1
        self.clear()
        self.write(f"Score is: {self.score}", align="center", font=("Arial", 24, "normal"))
