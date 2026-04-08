import random
from turtle import Turtle



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def next_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randint(-249, 249))
        new_car.setheading(180)
        self.all_cars.append(new_car)

    def move_car(self):
        for item in self.all_cars:
            item.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
