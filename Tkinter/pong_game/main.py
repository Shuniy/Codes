from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
from constants import GRID_HEIGHT, GRID_WIDTH, WIDTH, HEIGHT
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.colormode(255)
screen.setup(width=WIDTH + 30, height=HEIGHT + 30)
screen.title('Ping Pong: The Black Island')
screen.tracer(0)


def draw_grid():
    """Draws the grid"""
    grid_turtle = Turtle()
    grid_turtle.color('white')
    grid_turtle.penup()
    grid_turtle.speed('fast')
    grid_turtle.goto(GRID_WIDTH, GRID_HEIGHT)
    grid_turtle.pendown()
    grid_turtle.goto(-GRID_WIDTH, GRID_HEIGHT)
    grid_turtle.goto(-GRID_WIDTH, -GRID_HEIGHT)
    grid_turtle.goto(GRID_WIDTH, -GRID_HEIGHT)
    grid_turtle.goto(GRID_WIDTH, GRID_HEIGHT)
    grid_turtle.goto(0, GRID_HEIGHT)
    grid_turtle.goto(0, -GRID_HEIGHT)
    grid_turtle.hideturtle()


draw_grid()

left_paddle = Paddle('left')
right_paddle = Paddle('right')
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

# Right Paddle
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(right_paddle.go_left, "Left")
screen.onkey(right_paddle.go_right, "Right")

# Left Paddle
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(left_paddle.go_left, "a")
screen.onkey(left_paddle.go_right, "d")

# Ball
game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() >= GRID_HEIGHT - 10 or ball.ycor() <= -GRID_HEIGHT + 10:
        ball.bounce('walls')

    if ball.distance(left_paddle) < 60 and ball.xcor() < left_paddle.pos()[0] + 10 or \
            ball.distance(right_paddle) < 60 and ball.xcor() > right_paddle.pos()[0] - 10:
        ball.bounce('paddle')

    # ball miss (right paddle)
    if ball.xcor() >= GRID_WIDTH - 10:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() <= -GRID_WIDTH + 10:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
