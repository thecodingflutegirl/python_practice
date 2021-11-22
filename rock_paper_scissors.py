rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random 

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n'))


comp_choice = random.randint(0,2)

if choice == comp_choice:
  print('It is a tie!')
elif choice == 0:
  if comp_choice == 1:
    print(f'Computer wins! {paper} covers {rock}\nYou lose')
  elif comp_choice == 2:
    print(f'You win! {rock} beats {paper}')

elif choice == 1:
  if comp_choice == 0:
    print(f'You win!\n {paper} beats {rock}')
  elif comp_choice == 2:
    print(f'Computer wins!\n {scissors} beats {paper}\n You lose')
elif choice == 2: 
  if comp_choice == 0:
    print(f'Computer wins\n {rock} beats {scissors}\n You lose')
  elif comp_choice ==1:
    print(f'You win!\n {scissors} beats {paper}')
else: 
  print('invalid input, try again')
