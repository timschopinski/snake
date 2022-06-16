from turtle import Turtle



class Scoreboard(Turtle):

    ALIGNMENT = "center"
    FONT = ("Courier", 24, "normal")
    f = open("high_score.txt", 'r')

    high_score = f.read()
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} \t High score: {Scoreboard.high_score}", align=self.ALIGNMENT, font=self.FONT)


    def game_over(self):
        f = open("high_score.txt", "w")
        f.write(str(Scoreboard.high_score))
        f.close()
        self.goto(0, 0)
        self.write("GAME OVER", align=self.ALIGNMENT, font=self.FONT)

    def increase_score(self):
        self.score += 1
        if self.score > int(Scoreboard.high_score):
            Scoreboard.high_score = self.score
        self.clear()
        self.update_scoreboard()
