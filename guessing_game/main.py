
from art import logo
import random


START_GAME = True

def guess_checker(attempts):
        global START_GAME
        while attempts >0: # but if the guess is right and theres still attempts..the game should end not keep going? 
            print(f"You have {attempts} attempts remaining to guess the number")
            guess = int(input('Make a guess: '))
            if guess != correct_number:
                attempts -= 1
                if guess > correct_number:
                    print('Too high.\nGuess again.')
                else: 
                    print('Too low.\nGuess again.')
            else: 
                print(f'You guessed the number! It was {correct_number}')
                START_GAME = False

            if attempts == 0:
                print(f'You ran out of attempts! The correct number is {correct_number}')
                START_GAME = False

while START_GAME:

    correct_number = random.randint(1, 100)
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100")
    print(f"HINT: THE CORRECT NUMBER IS: {correct_number}")
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ')

    if difficulty == 'easy':
        attempts = 10
        guess_checker(attempts)

    elif difficulty == 'hard':
        attempts = 5
        guess_checker(attempts)

    else:
        print('Invalid input. Please start over')
        START_GAME = False
