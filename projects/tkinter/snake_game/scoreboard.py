from turtle import Turtle
from constants import SCOREBOARD_HEIGHT, FONT, ALIGNMENT


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, SCOREBOARD_HEIGHT)
        self.update_scoreboard()
        self.hideturtle()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score : {self.score}   |   High Score : {self.high_score}', align=ALIGNMENT,
                   font=FONT)

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write('Game Over', align=ALIGNMENT, font=FONT)

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
