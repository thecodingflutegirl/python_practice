from turtle import Turtle, Screen
import random 
racing = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(
    'Make your bet', 'Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtles = []
y = -100
for color in colors:
    new_turtle = Turtle('turtle')
    new_turtle.color(color)
    turtles.append(new_turtle)

for turtle in turtles:
    x = -230
    turtle.penup()
    turtle.goto(x, y)
    y += 42

if user_bet:
    racing = True 

while racing: 
    for turtle in turtles:
        if turtle.xcor() > 230:
            racing = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f'You won! The winning turtle is {winner}!')
            else:
                print(f'You lost! The winning turtle is {winner}!')
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
