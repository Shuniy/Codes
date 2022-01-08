from turtle import Turtle
from constants import GRID_HEIGHT


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('Green')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def scores(self):
        return [self.left_score, self.right_score]

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, GRID_HEIGHT - 110)
        self.write(self.left_score, align='center',
                   font=('Arial', 80, 'normal'))
        self.goto(300, GRID_HEIGHT - 110)
        self.write(self.right_score, align='center',
                   font=('Arial', 80, 'normal'))

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()
