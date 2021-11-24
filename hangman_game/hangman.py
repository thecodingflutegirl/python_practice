
from hangman_art import logo, stages, you_win, you_lose
import random
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
#print(f'HINT: this is the word: {chosen_word}')
lives = 6

display = []
for char in chosen_word:
    display += '_'


game_over = False
while not game_over:
    guess = input('Guess a letter: \n').lower()

    if guess in display:
        print(f"You've already guessed that letter: {guess}")
    # check guessed letter
    for i in range(len(chosen_word)):
        char = chosen_word[i]
        #print(f"Current position: {i}\n Current letter: {char}\n Guessed letter: {guess}")
        if char == guess:
            display[i] = char
    if guess not in chosen_word:  # must be this way and can't be if guess != char because != is used for ints, not strings

        print(f'The letter {guess} is not in the word. You lose one life.')
        lives -= 1

    if lives == 0:
        game_over = True
        print(you_lose)
        print(f"The word was {chosen_word}")

# Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if '_' not in display:
        game_over = True
        print(you_win)

    print(stages[lives])
