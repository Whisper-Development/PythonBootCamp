import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("green")

for i in range (15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = turtle.Screen()
screen.exitonclick()