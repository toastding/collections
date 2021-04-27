from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake game!")
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    # 2 -> 1 -> 0
    snake.move()

screen.exitonclick()

