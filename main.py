import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()

moving_up = False

def start_moving():
    global moving_up
    moving_up = True

def stop_moving():
    global moving_up
    moving_up = False
screen.listen()



screen.onkeypress(start_moving, "Up")
screen.onkeyrelease(stop_moving, "Up")
game_is_on = True
car_manager = CarManager()
# car_manager.next_car()
counter = 0
scoreboard = Scoreboard()
scoreboard.display_level()



while game_is_on:
    time.sleep(0.1)
    screen.update()
    if moving_up:
        turtle.move()
    counter += 1
    if counter % 6 == 0:
        car_manager.next_car()


    car_manager.move_car()
    for item in car_manager.all_cars:
        if item.distance(turtle) < 25:
            game_is_on = False
            scoreboard.game_over()
    if turtle.ycor() > 280:
        turtle.goto(player.STARTING_POSITION)
        car_manager.level_up()
        scoreboard.level_up()








screen.exitonclick()
