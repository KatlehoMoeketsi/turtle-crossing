import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player_one = Player()
score = Scoreboard()
car = CarManager()


game_is_on = True

screen.listen()
screen.onkey(player_one.move_up, "Up")
screen.onkey(player_one.move_down, "Down")

# Game loop
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Each iteration of loop makes a new car and tells them to move
    car.create_car()
    car.move_cars()

    #Detect successful crossing
    if player_one.ycor() > 230:
        player_one.reset_pos()
        car.level_up()
        score.score_up()


    #Detect collision with car
    for i in car.car_list:
        if i.distance(player_one) < 20:
            print("Splatt")
            score.game_over()
            game_is_on = False

screen.exitonclick()
