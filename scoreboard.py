from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_number = 1
        self.penup()
        self.hideturtle()

    def level_up(self):
        self.level_number += 1
        self.clear()
        self.write(f"Level: {self.level_number}", align="left", font=("Courier", 14, "bold"))


    def display_level(self):
        self.goto(-280, 270)
        self.write(f"Level: {self.level_number}", align="left", font=("Courier", 14, "bold"))


    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

