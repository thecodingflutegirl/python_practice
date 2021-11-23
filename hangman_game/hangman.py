# step 5
from hangman_art import logo, stages
import random


# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list
chosen_word = random.choice(word_list)
print(f'this is the word: {chosen_word}')
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

display = []
for char in chosen_word:
    display += '_'


game_over = False
while not game_over:
    guess = input('Guess a letter: \n').lower()
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed that letter: {guess}")
    # check guessed letter
    for i in range(len(chosen_word)):
        char = chosen_word[i]
        #print(f"Current position: {i}\n Current letter: {char}\n Guessed letter: {guess}")
        if char == guess:
            display[i] = char
    if guess not in chosen_word:  # must be this way and can't be if guess != char because != is used for ints, not strings
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'The letter {guess} is not in the word. You lose one life.')
        lives -= 1

    if lives == 0:
        game_over = True
        print('You lose!')

# Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if '_' not in display:
        game_over = True
        print('You win!')

# TODO-2: - Import the stages from hangman_art.py and make this error go away.

    print(stages[lives])
