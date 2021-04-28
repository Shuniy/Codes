from turtle import Turtle
from constants import MOVE_DISTANCE, STARTING_POSITIONS
from constants import UP, DOWN, LEFT, RIGHT


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape('square')

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.shapesize(stretch_len=1, stretch_wid=1)
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]