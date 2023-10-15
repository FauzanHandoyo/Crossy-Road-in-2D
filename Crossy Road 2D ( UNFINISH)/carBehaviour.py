from turtle import Turtle
import random

COLORS = ["red", "yellow", "green", "blue", "black", "orange"]
MOVE_INC = 10
MOVE_START = 10
CAR_RANGE = (-190, 210)
STRETCH_WID = (2, 4)

class CarBehaviour:

    def __init__(self):
        self.all_cars = []
        self.cars_speed = MOVE_START

    # creating random cars
    def create_car(self):
        random_car = random.randint(1, 5)
        if random_car == 1:
            new_car = Turtle("square")
            stretch_wid = random.randint(STRETCH_WID[0], STRETCH_WID[1])
            new_car.shapesize(stretch_wid, 1)  # Use both stretch_wid and stretch_len
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_speed = random.randint(CAR_RANGE[0], CAR_RANGE[1])
            new_car.setheading(-90)
            new_car.goto(300, random_speed)
            self.all_cars.append(new_car)

    # move cars to left side
    def move_cars(self):
        for car in self.all_cars:
            car.setx(car.xcor() - MOVE_INC)

    def level_up(self):
        self.cars_speed += MOVE_INC

    #check collision from chatgpt
    def check_collisions(self):
        for i in range(len(self.all_cars)):
            for j in range(i + 1, len(self.all_cars)):
                if self.all_cars[i].distance(self.all_cars[j]) < 50:  # Adjust the collision distance as needed
                    self.all_cars[i].setx(self.all_cars[i].xcor() + self.cars_speed)

