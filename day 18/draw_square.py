import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("green")

for i in range(4):
    timmy.forward(100)
    timmy.right(90)


screen = turtle.Screen()
screen.exitonclick()
