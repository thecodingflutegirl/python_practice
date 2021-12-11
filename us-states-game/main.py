import turtle
import pandas


screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        f'{len(guessed_states)}/50 States Correct', "What's another state?").title()

    data = pandas.read_csv("50_states.csv")
    states = data['state'].to_list()
    # x_cor = int(data['x'].to_list())
    # y_cor = int(data['y'].to_list())
    if answer_state == 'Exit':
        unlearned_states = []
        for state in states:
            if state not in guessed_states:
                unlearned_states.append(state)
        unlearned_data = pandas.DataFrane(unlearned_states)
        unlearned_data.to_csv('unlearned_states.csv')
        break
    if answer_state in states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)


screen.exitonclick()
