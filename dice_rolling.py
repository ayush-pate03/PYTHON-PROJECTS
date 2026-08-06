# loop
# Ask: roll the dice ?
# if user enters y
# genrate two random numbers 
# print them 
# if user enters n 
# print thank you message 
# terminate 
# else 
# print invalid choice
import random

while True :
 choice = input('Roll the dice? (y/n):  ').lower()
 if choice == 'y':
     die1 = random.randint(1, 6)
     die2 = random.randint(1, 6)
     print(f'({die1}, {die2})')
 elif choice == 'n':
     print("Thank You For Playing!")
     break
else :
     print("Invalid choice")