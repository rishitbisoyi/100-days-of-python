from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

text1=["Welcome to Snake Game!",
      "Use arrow keys to move the snake.",
      "Eat the blue food to grow!",
      "Don't hit the walls or yourself!",
      "Press x and click on screen to exit",
      "Game Starting...\nGood Luck!",]
text2=["3","2","1","Go!"]
t = Turtle()
t.hideturtle()
t.color("white")
for i in range(len(text1)):
    t.write(text1[i], align="center", font=("Arial", 24, "normal"))
    screen.update()
    time.sleep(2)
    t.clear()
for i in range(len(text2)):
    t.write(text2[i], align="center", font=("Arial", 24, "bold"))
    screen.update()
    time.sleep(1)
    t.clear()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def quit_game():
    global game_is_on
    game_is_on = False
screen.onkey(quit_game, "x")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            
scoreboard.save_high_score()
screen.exitonclick()


