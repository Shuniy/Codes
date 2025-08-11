from time import sleep
from turtle import Screen, Turtle

from constants import HEIGHT, WIDTH, GRID_HEIGHT, GRID_WIDTH, DOWN_RANGE, LEFT_RANGE, RIGHT_RANGE, UP_RANGE
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.colormode(255)
screen.setup(width=WIDTH + 30, height=HEIGHT + 30)
screen.bgcolor('black')
screen.title("Sandworm in a BOX")
screen.tracer(0)


# Drawing a grid


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
    grid_turtle.goto(GRID_WIDTH, UP_RANGE + 15)
    grid_turtle.goto(-GRID_WIDTH, UP_RANGE + 15)
    grid_turtle.hideturtle()


draw_grid()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increment_score()

    if snake.head.xcor() > (RIGHT_RANGE + 10) or snake.head.xcor() < (LEFT_RANGE - 10) \
            or snake.head.ycor() > (UP_RANGE + 10) or snake.head.ycor() < (DOWN_RANGE - 10):
        snake.reset()
        scoreboard.reset()

    # Collision with the tail or body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()
