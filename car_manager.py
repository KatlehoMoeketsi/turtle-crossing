from turtle import  Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITIONS = [(-230, -230), (-230, -200), (-230, -170),(-230, -140),(-230, -110),(-230, -70)]

class CarManager:
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.create_car()
        self.carspeed = STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.car_list:
            car.backward(STARTING_MOVE_DISTANCE)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT

    def reset_cars(self):
        self.goto(-230, -130)

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.car_list.append(new_car)