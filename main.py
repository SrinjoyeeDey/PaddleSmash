from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time         

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Mini Pong Game")
screen.tracer(0)

# we can create as many paddles as we want
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        # needs to bounce
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    # Detect when r paddle misses
    if ball.xcor()>380:
        ball.reset_pos()
        scoreboard.l_point()

    # Detect when l paddle misses
    if ball.xcor()<-380:
        ball.reset_pos()
        scoreboard.r_point()



screen.exitonclick()