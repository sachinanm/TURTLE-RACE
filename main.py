import turtle
from turtle import Turtle, Screen
import random
import tkinter

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race ? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
y_position = [-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.shape()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:

                tkinter.messagebox.showinfo("Result", f"You won! The winning color is {winning_color}")
            else:

                tkinter.messagebox.showinfo("Result", f"You lost. The winning color is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
