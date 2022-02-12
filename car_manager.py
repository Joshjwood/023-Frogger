from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def spawn_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(300, (random.randint(-250, 250)))
        self.all_cars.append(new_car)

    def move(self):
        for car in range(len(self.all_cars)):
            new_x = self.all_cars[car].xcor() - self.car_speed
            new_y = self.all_cars[car].ycor()
            self.all_cars[car].goto(new_x, new_y)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


