from art import logo, vs
from game_data import data
import random 


game = True
#while game:
choice_a = random.choice(data)
choice_b = random.choice(data)
current_score = 0 
print(logo)
print('Compare A: '+ choice_a['name']+ ', a ' + choice_a['description'] + ', from ' + choice_a['country'])
print(vs)
print('Against B: ' + choice_b['name']+ ', a ' + choice_b['description'] + ', from ' + choice_b['country'])
guess = input('Who has more followers? Type "A" or "B": ').upper()
print(choice_a['follower_count'])
print(choice_b['follower_count'])


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


# choices A and B need to be random, import random module and use randint() to generate random int
# compare A - Name, a DESCRIPTION from COUNTRY  Along with their stats and where they're from
# show the VS
# "Against B:" Whoever B is with their stats and stuff
# Ask user who has more followers? A or B?
#name, follower-count, description, country

#if A follower count is bigger or smaller
# if user is right their score goes up by 1 "You're right! Current score: {their score}"
# and then you do another round of A vs B, re show logo and vs
# if user is wrong the game ends and shows score "Sorry, that's wrong. Final score {the final or current? score}"
