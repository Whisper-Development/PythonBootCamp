import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()