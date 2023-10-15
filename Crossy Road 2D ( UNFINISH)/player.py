from turtle import Turtle

STARTING_POS = (0, -250)
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POS)
    
    def finish_line(self, finish_line):
        if self.ycor >= finish_line:
            return True
        else:
            return False