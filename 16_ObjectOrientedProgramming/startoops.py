# import turtle
# # from turtle import Turtle,Screen

# timmy=turtle.Turtle()
# # timmy=Turtle()
# # print(timmy)

# my_screen=turtle.Screen()
# # my_screen=Turtle()
# # print(my_screen)
# # print(my_screen.canvheight)
# # print(my_screen.canvwidth)

# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

table=PrettyTable()
# print(table)

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="l"
print(table)