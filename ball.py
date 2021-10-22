from turtle import Turtle, Screen
import time
from score_pong import Score

score = Score()

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.self = []
        self.penup()
        self.goto(0, 0)
        self.shape('circle')
        self.color('white')
        self.speed(1)

    def ball_move(self):
        self.forward(10)

    def ball_clear(self):
        self.hideturtle()

    def increase_speed(self):
        self.speed(int(self.speed())+1)

    def bounce(self):
        """print(self.heading())"""
        if 0 < self.heading() < 90:
            self.setheading(360 - (self.heading()))
        elif 90 < self.heading() < 180:
            self.setheading((180 - self.heading()) + 180)
        elif 180 < self.heading() < 270:
            self.setheading(180-(self.heading()-180))
        elif 270 < self.heading() < 360:
            self.setheading(360 - self.heading())

    def bounce_back(self):
        """print(self.heading())"""
        if 0 < self.heading() < 90:
            self.setheading(180 - self.heading())
        elif 90 < self.heading() < 180:
            self.setheading(180 - self.heading())
        elif 180 < self.heading() < 270:
            self.setheading(360-(self.heading()-180))
        elif 270 < self.heading() < 360:
            self.setheading((360 - self.heading()) + 180)

    def game_over(self):
        tim = Turtle()
        tim.hideturtle()
        tim.width(3)
        tim.color('cyan')
        for i in range(0, 3):
            tim.clear()
            tim.write(f"Starting in {3 - i}", align='center', font=("Arial", "30", "normal"))
            time.sleep(1)
        tim.clear()
        self.ball_clear()

    def game_over_real(self, player):
        tim = Turtle()
        tim.hideturtle()
        tim.color('white')
        if player == 1:
            tim.write(f"Player 2 wins", align='center', font=("Arial", "30", "normal"))
        elif player == 2:
            tim.write(f"Player 1 wins", align='center', font=("Arial", "30", "normal"))