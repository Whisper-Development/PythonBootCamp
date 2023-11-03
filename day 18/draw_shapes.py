import turtle
import random

timmy = turtle.Turtle()

colours = ["Blue", "Purple", "Red", "Green", "DarkBlue", "DarkOrchid", "CornflowerBlue", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3,10):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = turtle.Screen()
screen.exitonclick()