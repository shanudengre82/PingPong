import turtle
from turtle import Turtle, Screen

screen = Screen()


class Bars(Turtle):

    def __init__(self):
        super().__init__()
        self.bars = []
        self.create_bars()
        self.center_line()

    def create_bars(self):
        for i in range(0, 2):
            tim = Turtle()
            tim.hideturtle()
            tim.penup()
            tim.shape('square')
            tim.shapesize(stretch_len=5, stretch_wid=1)
            tim.color('white')
            tim.goto(480*(-1)**i, 0)
            tim.setheading(90)
            tim.showturtle()
            self.bars.append(tim)

    def move_up_1(self):
        self.speed('fastest')
        self.bars[0].goto(self.bars[0].xcor(), int(self.bars[0].ycor())+50)
        if self.bars[0].position()[1] > 360:
            self.bars[0].goto(480, 360)

    def move_down_1(self):
        self.speed('fastest')
        self.bars[0].goto(self.bars[0].xcor(), int(self.bars[0].ycor()) - 50)
        if self.bars[0].position()[1] < -360:
            self.bars[0].goto(480, -360)

    def move_up_2(self):
        self.speed('fastest')
        self.bars[1].goto(self.bars[1].xcor(), int(self.bars[1].ycor()) + 50)
        if self.bars[1].position()[1] > 360:
            self.bars[1].goto(-480, 360)

    def move_down_2(self):
        self.speed('fastest')
        self.bars[1].goto(self.bars[1].xcor(), int(self.bars[1].ycor()) - 50)
        if self.bars[1].position()[1] < -360:
            self.bars[1].goto(-480, -360)

    def center_line(self):
        self.setheading(90)
        self.penup()
        self.width(3)
        self.color('white')
        self.goto(0, 400)
        self.setheading(270)
        while self.ycor() >= -400:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.hideturtle()


