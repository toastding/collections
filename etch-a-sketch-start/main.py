from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def back_forwards():
    tim.forward(-10)


def counter_clockwise():
    tim.circle(60, 10)


def clockwise():
    tim.circle(-60, 10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.setpos(0, 0)
    tim.setheading(0)
    tim.pendown()


screen.listen()
screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=back_forwards)
screen.onkey(key="A", fun=counter_clockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=clear_drawing)
screen.exitonclick()
