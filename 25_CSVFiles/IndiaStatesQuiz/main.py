from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("India States Quiz")
screen.setup(width=900, height=1050)

image = "25_CSVFiles/IndiaStatesQuiz/map.gif"
screen.addshape(image)

map_turtle = Turtle()
map_turtle.shape(image)

writer = Turtle()
writer.hideturtle()
writer.penup()

data = pd.read_csv("25_CSVFiles/IndiaStatesQuiz/states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{len(all_states)} States Correct",
        prompt="Enter a state name:"
    )
    if answer_state is None:
        break
    answer_state = answer_state.lower().strip()
    if answer_state == "Exit":
        missing_states = [
            state
            for state in all_states
            if state not in guessed_states
        ]
        pd.DataFrame(missing_states).to_csv(
            "25_CSVFiles/IndiaStatesQuiz/states_to_learn.csv",
            index=False
        )
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        x = int(state_data.x.iloc[0])
        y = int(state_data.y.iloc[0])
        writer.goto(x, y)
        writer.write(
            answer_state,
            align="center",
            font=("Arial", 10, "bold")
        )
if len(guessed_states) == len(all_states):
    writer.goto(0, 0)
    writer.write(
        "Congratulations!\nYou found all States and UTs!",
        align="center",
        font=("Arial", 18, "bold")
    )
screen.exitonclick()