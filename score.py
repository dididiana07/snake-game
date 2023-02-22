import turtle


def game_over():
    game_over_label = turtle.Turtle()
    game_over_label.hideturtle()
    game_over_label.color("red")
    game_over_label.penup()
    game_over_label.write(arg="Game Over", align="center", font=("Helvetica", 40, "normal"))
    game_over_label.setposition(0, 0)


class Score:
    def __init__(self):
        self.score = 0
        self.score_label = turtle.Turtle()
        self.score_label.color("white")
        self.score_label.penup()
        self.score_label.hideturtle()
        self.score_label.setpos(-250, 250)
        self.score_label.write(arg=f"Score: {self.score}",
                               align="center", font=('Helvetica', 25, 'normal'))

        with open("high_score.txt") as file:
            self.high_score = int(file.readline())
        self.high_score_label = turtle.Turtle()
        self.high_score_label.color("white")
        self.high_score_label.penup()
        self.high_score_label.hideturtle()
        self.high_score_label.setpos(220, 250)
        self.high_score_label.write(arg=f"High score: {self.high_score}",
                                    align="center", font=('Helvetica ', 25, 'normal'))

    def add_score(self):
        self.score += 1
        self.score_label.clear()
        self.score_label.write(arg=f"Score: {self.score}", align="center", font=('Arial', 25, 'normal'))

    def check_high_score(self):
        if self.score > self.high_score:
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))

    def restart_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write("0")
        self.high_score_label = 0




