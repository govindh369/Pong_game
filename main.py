from turtle import Screen
from paddle import Paddle
from Pong_game.ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
# screen.tracer(1)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()
    # detect collision with ball and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    # detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
