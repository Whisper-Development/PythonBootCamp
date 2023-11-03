import turtle
import random
import colorgram

timmy = turtle.Turtle()
turtle.colormode(255)

rgb_colors = []

colors = colorgram.extract('day 18\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dots in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)

    if dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
