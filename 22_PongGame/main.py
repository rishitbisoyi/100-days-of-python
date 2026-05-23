from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
t = Turtle()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
t.color("white")
t.hideturtle()
t.penup()

num_rounds=screen.textinput(title="Pong Game", prompt="Enter the number of rounds to play (default is 1): ")
if num_rounds is None or not num_rounds.isdigit():
    t.goto((0,0))
    t.write("Invalid input. Defaulting to 1 round.", align="center", font=("Arial", 16, "normal"))
    screen.update()
    time.sleep(2)
    t.clear()
    num_rounds = 1
else:
    num_rounds = int(num_rounds)

num_score=screen.textinput(title="Pong Game", prompt="Enter the score needed to win (default is 5): ")
if num_score is None or not num_score.isdigit():
    t.goto((0,0))
    t.write("Invalid input. Defaulting to 5 points.", align="center", font=("Arial", 16, "normal"))
    screen.update()
    time.sleep(2)
    t.clear()
    num_score = 5
else:
    num_score = int(num_score)


t.goto((0,220))
t.write("Left Player: W/S | Right Player: Up/Down", align="center", font=("Arial", 16, "normal"))
screen.update()
time.sleep(3)
t.clear()

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboardl = Scoreboard((-150, 220))
scoreboardr = Scoreboard((150, 220))

screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

rounds_left = 0
rounds_right = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if (ball.xcor() > 320 and ball.distance(right_paddle) < 50) or (ball.xcor() < -320 and ball.distance(left_paddle) < 50):
        ball.bounce_x()
    if ball.xcor() > 390:
        scoreboardl.increase_score()
        if scoreboardl.score >= num_score:
            rounds_left += 1
            t.goto(0, 0)
            t.write("Left Player Wins!", align="center", font=("Arial", 24, "normal"))
            screen.update()
            time.sleep(3)
            t.clear()
            t.write(f"Rounds: Left Player {rounds_left} - Right Player {rounds_right}", align="center", font=("Arial", 16, "normal"))
            screen.update()
            time.sleep(2)
            t.clear()
            if rounds_left >= num_rounds:
                game_is_on = False
            scoreboardl.reset_score()
            scoreboardr.reset_score()
        ball.reset()
    elif ball.xcor() < -390:
        scoreboardr.increase_score()
        if scoreboardr.score >= num_score:
            rounds_right += 1
            t.goto(0, 0)
            t.write("Right Player Wins!", align="center", font=("Arial", 24, "normal"))
            screen.update()
            time.sleep(3)
            t.clear()
            t.write(f"Rounds: Left Player {rounds_left} - Right Player {rounds_right}", align="center", font=("Arial", 16, "normal"))
            screen.update()
            time.sleep(2)
            t.clear()
            if rounds_right >= num_rounds:
                game_is_on = False
            scoreboardl.reset_score()
            scoreboardr.reset_score()
        ball.reset()

t.clear()
if rounds_left >= num_rounds:
    t.goto(0, 0)
    t.write("Left Player Wins the Match!\n\n(Click on screen to exit)", align="center", font=("Arial", 24, "normal"))
elif rounds_right >= num_rounds:
    t.goto(0, 0)
    t.write("Right Player Wins the Match!\n\n(Click on screen to exit)", align="center", font=("Arial", 24, "normal"))
screen.exitonclick()

