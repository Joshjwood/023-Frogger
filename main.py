import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

spawn_counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    spawn_counter += 1

    if spawn_counter % 6 == 1:
        car_manager.spawn_car()
    car_manager.move()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 300:
        car_manager.level_up()
        player.reset_player()
        scoreboard.end_zone()




screen.exitonclick()
