from constants import GRID_HEIGHT, GRID_WIDTH, WIDTH, HEIGHT
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.bgcolor('black')
screen.setup(width=WIDTH + 20, height=HEIGHT + 20)
screen.tracer(0)


def draw_grid():
    """Draws the grid"""
    grid_turtle = Turtle()
    grid_turtle.color('white')
    grid_turtle.penup()
    grid_turtle.goto(GRID_WIDTH, GRID_HEIGHT)
    grid_turtle.pendown()
    grid_turtle.goto(-GRID_WIDTH, GRID_HEIGHT)
    grid_turtle.goto(-GRID_WIDTH, -GRID_HEIGHT)
    grid_turtle.goto(GRID_WIDTH, -GRID_HEIGHT)
    grid_turtle.goto(GRID_WIDTH, GRID_HEIGHT)
    grid_turtle.hideturtle()


draw_grid()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')
screen.onkey(player.go_left, 'Left')
screen.onkey(player.go_right, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # Successfully crossed
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increment_level()

screen.exitonclick()
