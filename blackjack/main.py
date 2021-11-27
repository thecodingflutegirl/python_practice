import random
from art import logo 

print(logo)
start_game = input('Do you want to play a game of Blackjack? Type "y" for yes or "n" for no. \n').lower()



def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards =[]
    user_cards += random.choices(cards, k=2)
    computer_cards += random.choices(cards, k=2)
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    
    if user_cards != [11, 10] or computer_cards != [11, 10]:
        if user_score > 21 or computer_score > 21:
            cards[0] = 1
    elif user_cards != [11, 10] and computer_cards == [11, 10]:
        print('Computer wins by Blackjack! You lose :(')
    elif computer_cards != [11, 10] and user_cards == [11,10]:
        print('You win by Blackjack! :) Computer loses')

if start_game == 'y':
    blackjack()
    