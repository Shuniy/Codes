from turtle import Turtle

from constants import FONT
from constants import GRID_HEIGHT, GRID_WIDTH


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-GRID_WIDTH + 50, GRID_HEIGHT - 50)
        self.color('green')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'level : {self.level}', align="left", font=FONT)

    def increment_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)
