from turtle import Turtle

FONT = ("Courier", 22, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(-280, 250)
        self.write(arg=f"Score:{self.score} ", align=ALIGNMENT, font=FONT)


    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(arg=f"Score:{self.score} ", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align="center", font=FONT)
