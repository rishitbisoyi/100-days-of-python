from turtle import Turtle
import time

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Welcome to Snake Game!", align="center", font=("Arial", 24, "normal"))
        self.getscreen().update()
        time.sleep(3)
        self.clear()
        self.write("Use arrow keys to move the snake.", align="center", font=("Arial", 16, "normal"))
        self.getscreen().update()
        time.sleep(3)
        self.clear()
        self.write("Eat the blue food to grow!", align="center", font=("Arial", 16, "normal"))
        self.getscreen().update()
        time.sleep(3)
        self.clear()
        self.write("Don't hit the walls or yourself!", align="center", font=("Arial", 16, "normal"))
        self.getscreen().update()
        time.sleep(3)
        self.clear()
        self.write("Game Starting...", align="center", font=("Arial", 24, "normal"))
        self.getscreen().update()
        time.sleep(2)
        self.clear()   
        self.write("Good Luck!", align="center", font=("Arial", 24, "normal"))
        self.getscreen().update()
        time.sleep(2)
        self.clear()  
        self.write("Go!", align="center", font=("Arial", 24, "normal"))
        self.getscreen().update()
        time.sleep(1)
        self.clear() 
        self.write("3", align="center", font=("Arial", 24, "normal"))
        self.getscreen().update()
        time.sleep(1)
        self.clear()
        self.write("2", align="center", font=("Arial", 24, "normal"))
        self.getscreen().update()
        time.sleep(1)
        self.clear()
        self.write("1", align="center", font=("Arial", 24, "normal"))
        self.getscreen().update()
        time.sleep(1)
        self.clear()
        self.write("Start!", align="center", font=("Arial", 24, "normal"))
        self.getscreen().update()
        time.sleep(1)
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 36, "bold"))