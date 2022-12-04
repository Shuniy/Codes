import random

WIDTH = 900
HEIGHT = 900

GRID_WIDTH = WIDTH // 2
GRID_HEIGHT = HEIGHT // 2

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

FONT = ("Roboto", 24, "normal")

STARTING_POSITION = (0, -GRID_HEIGHT + 20)
MOVE_DISTANCE = 10
FINISH_LINE_Y = GRID_HEIGHT - 20


def generate_random_color():
    color = [10, 10, 10]
    color[0] = random.randint(33, 255)
    color[1] = random.randint(33, 255)
    color[2] = random.randint(33, 255)
    return color
