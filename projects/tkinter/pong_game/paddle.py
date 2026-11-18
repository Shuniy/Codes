from turtle import Turtle
from constants import GRID_WIDTH, GRID_HEIGHT, PADDLE_SPEED


class Paddle(Turtle):
    def __init__(self, place) -> None:
        super().__init__()
        self.shape('square')
        self.place = place

        if self.place == 'right':
            self.color('blue')
        else:
            self.color('red')

        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()

        if self.place == 'right':
            self.goto(GRID_WIDTH - 30, 0)
        elif self.place == 'left':
            self.goto(-GRID_WIDTH + 30, 0)

    def go_up(self):
        new_y = self.ycor() + PADDLE_SPEED
        if new_y <= GRID_HEIGHT - 50:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - PADDLE_SPEED
        if new_y >= -GRID_HEIGHT + 50:
            self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() - PADDLE_SPEED
        if self.place == 'right':
            if new_x >= 0 + 20:
                self.goto(new_x, self.ycor())
        else:
            if new_x >= -GRID_WIDTH + 20:
                self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + PADDLE_SPEED
        if self.place == 'right':
            if new_x <= GRID_WIDTH - 20:
                self.goto(new_x, self.ycor())
        else:
            if new_x <= 0 - 20:
                self.goto(new_x, self.ycor())
