from turtle import Turtle, Screen
# Draw regular polygons using Turtle Graphics
timmy = Turtle()
timmy.shape("arrow")
distance = 100
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def my_fun(sides, alternate_angle):
    timmy.forward(distance)
    for i in range(1, sides):
        timmy.right(alternate_angle)
        timmy.forward(distance)
    timmy.right(alternate_angle)

# alternate_angle = 180 - actual_angle

# For a Triangle
my_fun(3,120)

# For a Square
my_fun(4,90)

# For a Pentagon
my_fun(5,72)

# For a Hexagon
my_fun(6,60)

# For a Heptagon
my_fun(7,51.428)

# For an Octagon
my_fun(8,45)

# For a Nonagon
my_fun(9,40)

# For a Decagon
my_fun(10,36)

# How to show on screen
show = Screen()
show.exitonclick()
