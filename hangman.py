#step 3
import random 
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
for char in chosen_word:
     display += '_'

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
game_over = False
while not game_over: 
    guess = input('Guess a letter: \n').lower()

    #check guessed letter 
    for i in range(len(chosen_word)):
        char = chosen_word[i]
        #print(f"Current position: {i}\n Current letter: {char}\n Guessed letter: {guess}")
        if char == guess:
            display[i] = char


    print(display)

    if '_' not in display:
        game_over == True
        print('You win!')