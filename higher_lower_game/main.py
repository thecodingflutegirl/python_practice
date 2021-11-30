from art import logo, vs
from game_data import data
import random
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


game = True
current_score = 0
choice_b = random.choice(data)

while game:
    choice_a = choice_b
    choice_b = random.choice(data)

    print(logo)
    print('Compare A: ' + choice_a['name'] + ', a ' +
          choice_a['description'] + ', from ' + choice_a['country'])
    print(vs)
    print('Against B: ' + choice_b['name'] + ', a ' +
          choice_b['description'] + ', from ' + choice_b['country'])
    guess = input('Who has more followers? Type "A" or "B": ').upper()
    print(choice_a['follower_count'])
    print(choice_b['follower_count'])
    clearConsole()

    if choice_a['follower_count'] > choice_b['follower_count']:
        if guess == 'A':
            current_score += 1
            print(f"You're right! Current score: {current_score}")
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game = False

    if choice_a['follower_count'] < choice_b['follower_count']:
        if guess == 'B':
            current_score += 1
            print(f"You're right! Current score: {current_score}")
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game = False
