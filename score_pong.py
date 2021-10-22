from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0

    def increase_score(self, player=0):
        if player == 1:
            self.score_1 += 1
        elif player == 2:
            self.score_2 += 1
        else:
            pass
        self.clear()
        self.hideturtle()
        self.width(3)
        self.color('cyan')
        self.penup()
        self.goto(250, 340)
        self.pendown()
        self.write(f"{self.score_1}", align='center', font=("Arial", "40", "normal"))
        self.penup()
        self.goto(-250, 340)
        self.pendown()
        self.write(f"{self.score_2}", align='center', font=("Arial", "40", "normal"))
        self.penup()
