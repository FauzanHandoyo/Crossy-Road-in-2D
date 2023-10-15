from turtle import Screen, Turtle
from player import Player
from carBehaviour import CarBehaviour
from scoreboard import Scoreboard
import mainMenu
import time
import keyboard

def show_menu():  # Define show_menu function here
    mainMenu.show_menu()

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
car_behaviour = CarBehaviour()
scoreboard = Scoreboard(show_menu)  # Pass the show_menu function as an argument

finish_line = 290
isGameNotOver = True

# Create a finish line marker
finish_line_marker = Turtle()
finish_line_marker.penup()
finish_line_marker.goto(-400, finish_line)
finish_line_marker.pendown()
finish_line_marker.color("black")
finish_line_marker.pensize(5)
finish_line_marker.forward(800)

while isGameNotOver:
    time.sleep(0.1)
    screen.update()

    if keyboard.is_pressed("w"):
        player.move_forward()

    car_behaviour.create_car()
    car_behaviour.move_cars()

    for car in car_behaviour.all_cars:
        if car.distance(player) < 20:
            isGameNotOver = False
            scoreboard.game_over()
    
    if player.ycor() >= finish_line:
        player.reset()
        car_behaviour.level_up()
        scoreboard.increase_level()

    car_behaviour.check_collisions()

screen.exitonclick()
