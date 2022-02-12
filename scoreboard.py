from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1

        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", False, align="Center", font=("Arial", 24, "normal"))

    def end_zone(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.write(arg="Game Over", align="Center", font=("Arial", 24, "normal"))
