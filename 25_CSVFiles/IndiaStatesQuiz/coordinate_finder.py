from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=900, height=1050)
image = "25_CSVFiles/IndiaStatesQuiz/map.gif"
screen.addshape(image)

map_turtle = Turtle()
map_turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(f"{x},{y}")

screen.onscreenclick(get_mouse_click_coor)

screen.mainloop()