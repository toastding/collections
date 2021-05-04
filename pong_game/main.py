from turtle import Screen
from paddle import Paddle
import time

paddle = Paddle()
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()


