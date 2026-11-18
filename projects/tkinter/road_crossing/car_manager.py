import random
from constants import MOVE_INCREMENT
from constants import STARTING_MOVE_DISTANCE, generate_random_color
from turtle import Turtle
from constants import GRID_HEIGHT, GRID_WIDTH


class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 9)
        if random_chance == 3:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            colors = generate_random_color()
            new_car.color(colors[0], colors[1], colors[2])
            random_y = random.randint(-GRID_HEIGHT + 30, GRID_HEIGHT - 30)
            new_car.goto(GRID_WIDTH - 5, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
            if car.xcor() < -GRID_WIDTH + 5:
                random_y = random.randint(-GRID_HEIGHT + 30, GRID_HEIGHT - 30)
                car.goto(GRID_WIDTH - 5, random_y)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
