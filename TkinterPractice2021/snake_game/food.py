from turtle import Turtle
import random
from constants import DOWN_RANGE, UP_RANGE, LEFT_RANGE, RIGHT_RANGE


def generate_random_color():
    color = [10, 10, 10]
    color[0] = random.randint(33, 255)
    color[1] = random.randint(33, 255)
    color[2] = random.randint(33, 255)
    return color


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        colors = generate_random_color()
        self.color(colors[0], colors[1], colors[2])
        random_x = random.randint(LEFT_RANGE, RIGHT_RANGE)
        random_y = random.randint(DOWN_RANGE, UP_RANGE)
        self.goto(random_x, random_y)
