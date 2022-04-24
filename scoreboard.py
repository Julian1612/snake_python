from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.high_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score_board()

    def refresh_score(self):
        self.goto(0, 260)
        self.clear()
        self.score += 1
        self.update_score_board()