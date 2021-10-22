import turtle
import numpy as np
import random
from turtle import Turtle, Screen
from bars_ import Bars
import time
from ball import Ball
from score_pong import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1000, height=800)

bar = Bars()
score = Score()
ball = Ball()
ball.setheading(random.randint(0, 360))
while 65 < ball.heading() < 115 or 235 < ball.heading() < 295:
    ball.setheading(random.randint(0, 360))

screen.listen()
screen.onkeypress(key="Up", fun=bar.move_up_1)
screen.onkeypress(key='Down', fun=bar.move_down_1)
screen.onkeypress(key="w", fun=bar.move_up_2)
screen.onkeypress(key='s', fun=bar.move_down_2)

"""print(ball.heading())"""

game_on = True
screen_delay_factor = 100
while game_on:
    ball.ball_move()
    if 0 <= ball.heading() < 5:
        ball.setheading(20)
    if 355 <= ball.heading() < 0:
        ball.setheading(370)
    ball.speed('fastest')
    time.sleep(0.02*(0.01*screen_delay_factor))
    screen.delay(0.3)
    screen.update()
    if ball.ycor() >= 350 or ball.ycor() <= -350:
        ball.bounce()
    """print(ball.xcor(), ball.ycor())
    print(int(bar.bars[0].xcor()), int(bar.bars[0].ycor()))
    print(int(bar.bars[1].xcor()), int(bar.bars[1].ycor()))"""
    if int(ball.xcor()) in range(-463, -457) and int(ball.ycor()) \
            in range(int(bar.bars[1].ycor()) - 56, int(bar.bars[1].ycor()) + 56):
        print(ball.xcor(), ball.ycor())
        print(bar.bars[1].xcor(), bar.bars[1].ycor())
        print("True")
        ball.bounce_back()
        ball.increase_speed()
        print(ball.speed())
        if screen_delay_factor > 10:
            screen_delay_factor -= 5
        if 1 <= screen_delay_factor < 10:
            screen_delay_factor -= 1
        if 0.1 < screen_delay_factor < 1:
            screen_delay_factor -= 0.1
        if screen_delay_factor == 0.1:
            screen_delay_factor = 0.1

    if int(ball.xcor()) in range(457, 463) and int(ball.ycor()) \
            in range(int(bar.bars[0].ycor()) - 56, int(bar.bars[0].ycor()) + 56):
        print(ball.xcor(), ball.ycor())
        print(bar.bars[0].xcor(), bar.bars[0].ycor())
        print("False")
        ball.bounce_back()
        ball.increase_speed()
        print(ball.speed())
        if screen_delay_factor > 10:
            screen_delay_factor -= 5
        if 1 <= screen_delay_factor < 10:
            screen_delay_factor -= 1
        if 0.1 < screen_delay_factor < 1:
            screen_delay_factor -= 0.1
        if screen_delay_factor == 0.1:
            screen_delay_factor = 0.1

    if ball.distance(bar.bars[0]) < 15 or ball.distance(bar.bars[1]) < 15:
        ball.bounce_back()

    if ball.xcor() > 485:
        screen_delay_factor = 100
        ball.goto(490, ball.ycor())
        score.increase_score(player=2)
        if score.score_2 == 5:
            ball.game_over_real(player=2)
            game_on = False
        else:
            ball.game_over()
            ball = Ball()
            ball.setheading(random.randint(0, 360))
            while 65 < ball.heading() < 115 or 235 < ball.heading() < 295:
                ball.setheading(random.randint(0, 360))

    if ball.xcor() < -485:
        screen_delay_factor = 100
        ball.goto(-485, ball.ycor())
        score.increase_score(player=1)
        if score.score_1 == 5:
            ball.game_over_real(player=1)
            game_on = False
        else:
            ball.game_over()
            ball = Ball()
            ball.setheading(random.randint(0, 360))
            while 65 < ball.heading() < 115 or 235 < ball.heading() < 295:
                ball.setheading(random.randint(0, 360))


screen.exitonclick()












