from constants import GRID_HEIGHT, GRID_WIDTH
from constants import FINISH_LINE_Y
from constants import MOVE_DISTANCE
from constants import STARTING_POSITION, generate_random_color
from turtle import Turtle


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        colors = generate_random_color()
        self.color(colors[0], colors[1], colors[2])
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def boundary_check(self):
        if GRID_HEIGHT > self.ycor() > -GRID_HEIGHT and GRID_WIDTH > self.xcor() > -GRID_WIDTH:
            return True
        else:
            return False

    def go_up(self):
        if self.boundary_check():
            self.forward(MOVE_DISTANCE)
        else:
            self.go_to_start()

    def go_down(self):
        if self.boundary_check():
            self.backward(MOVE_DISTANCE)
        else:
            self.go_to_start()

    def go_left(self):
        self.left(MOVE_DISTANCE)

    def go_right(self):
        self.right(MOVE_DISTANCE)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
