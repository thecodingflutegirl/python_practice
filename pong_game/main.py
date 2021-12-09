from turtle import Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


game = True
while game:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor()< -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
        

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        


screen.exitonclick()