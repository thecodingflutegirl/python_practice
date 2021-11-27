import random
from art import logo
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


print(logo)
start_game = input(
    'Do you want to play a game of Blackjack? Type "y" for yes or "n" for no. \n').lower()


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    user_cards += random.choices(cards, k=2)
    computer_cards += random.choices(cards, k=2)
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    if user_cards != [11, 10] or computer_cards != [11, 10]:
        if user_score > 21 or computer_score > 21:
            cards[0] = 1

        print(
            f'Your cards are: {user_cards}, and current score of: {user_score}')
        print(f'The computer has a card of: {computer_cards[0]}')

        add_card = True
        if user_score > 21:
            add_card = False
            print('You lose! :(')

        while user_score <= 21 and add_card:
            new_card = input(
                'Would you like to draw another card? Type "y" or "n"\n')
            if new_card == 'y':
                user_cards.append(random.choice(cards))
                user_score = sum(user_cards)
                if user_score <= 21:
                    print(
                        f'Your new current cards are: {user_cards} with a score of {user_score}')
                    print(f'The computer has a card of: {computer_cards[0]}')

            else:
                add_card = False

        while computer_score < 17:
            computer_cards.append(random.choice(cards))
            computer_score = sum(computer_cards)
            if computer_score > 21:
                print('Computer went over. User wins!')

        print(
            f'Your final cards are: {user_cards} with a score of: {user_score}')
        print(
            f'The computer has cards of: {computer_cards} and a score of: {computer_score}')

        if user_score > 21:
            print('You went over! You lose :(')
        elif computer_score > 21:
            print('Computer went over. You win!')
        elif user_score > computer_score:
            print('User has higher score! You win! :)')
        elif computer_score > user_score:
            print('Computer has higher score! You loser! :(')

    another_game = input(
        'Do you want to play another game of Blackjack? Type "y" or "n"\n')
    if another_game == 'y':
        clearConsole()
        blackjack()

    elif user_cards != [11, 10] and computer_cards == [11, 10]:
        print('Computer wins by Blackjack! You lose :(')
    elif computer_cards != [11, 10] and user_cards == [11, 10]:
        print('You win by Blackjack! :) Computer loses')


if start_game == 'y':
    blackjack()
