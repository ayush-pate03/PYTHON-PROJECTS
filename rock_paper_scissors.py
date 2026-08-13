# ask the user to make a choice
# if choice is not valid
# print an error 
# let the computer to make choice
# print choices 
# determine the winner 
# ask the user if you want to continue 
# if not 
# terminate 
import random

choices = ('r', 'p', 's')

while True:
    user_choice = input('Rock, paper, or Scissors? (r/p/s): ').lower()
    
    if user_choice not in choices:
        print('INVALID CHOICE!')
        continue  
        
    computer_choice = random.choice(choices)
    print(f'You chose {user_choice}')
    print(f'computer chose {computer_choice}')
    
    if user_choice == computer_choice:
        print('Tie')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')
    ):
        print('You Win!')
    else:
        print('You Lose!')
        
    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break