from turtle import Screen
from paddle import Paddle
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()


