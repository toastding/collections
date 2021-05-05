from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.goto(0, 0)
        self.color("white")

    def move(self):
        self.penup()
        if self.xcor() != 300 and self.ycor() != 400:
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)