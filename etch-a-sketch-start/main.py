from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def back_forwards():
    tim.backward(10)


def counter_clockwise():
    tim.circle(60, 10)


def clockwise():
    tim.circle(-60, 10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=back_forwards)
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(key="q", fun=counter_clockwise)
screen.onkey(key="e", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
