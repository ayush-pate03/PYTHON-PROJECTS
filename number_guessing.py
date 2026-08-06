# genrate a random number 
#loop
  #ask user to make guess
  # if not a valid number 
  # print an error 
  # if number <guess 
  # print to low 
  # if number > guess 
  # print too high
  # else 
  # print well done 
import random

number_to_guess = random.randint(1, 100)
while True:
  try:
    guess= int(input('Guess the number between 1 to 100:  '))
  
    if guess < number_to_guess :
      print('Too low')
    elif guess > number_to_guess:
     print("To high")  
    else:
     print("Congrattulation! You guess it ")
     break
  except ValueError :
   print("Please enter a valid number")

