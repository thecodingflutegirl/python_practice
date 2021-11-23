#step 4
import random 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

lives = 6
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

display = []
for char in chosen_word:
     display += '_'


game_over = False
while not game_over: 
    guess = input('Guess a letter: \n').lower()

    #check guessed letter 
    for i in range(len(chosen_word)):
        char = chosen_word[i]
        #print(f"Current position: {i}\n Current letter: {char}\n Guessed letter: {guess}")
        if char == guess:
            display[i] = char
    if guess not in chosen_word: # must be this way and can't be if guess != char because != is used for ints, not strings
        lives = lives -1
        print(lives)
        
        
    if lives == 0:
        game_over = True
        print('You lose!')
#TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if '_' not in display:
        game_over = True
        print('You win!')

    print(stages[lives])
   
#TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    