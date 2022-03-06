from constants import BALL_SPEED
from turtle import Turtle
import random


def generate_random_color():
    color = [10, 10, 10]
    color[0] = random.randint(33, 255)
    color[1] = random.randint(33, 255)
    color[2] = random.randint(33, 255)
    return color


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_speed = BALL_SPEED
        self.y_speed = BALL_SPEED

    def change_color(self):
        colors = generate_random_color()
        self.color(colors[0], colors[1], colors[2])

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce(self, collision_type):
        self.change_color()
        if 'walls' == collision_type:
            self.y_speed *= -1
        elif 'paddle' == collision_type:
            self.x_speed *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce('paddle')
