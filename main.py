# Elite 101 Chatbot
#Importing necessary libraries
import random
import sys

global in_use
in_use = True
#Introduction to chatbot and receiving the user's name and age
#Initializing the conversation
print('Welcome to THE chatbot for banking!')

name = input("For starters, what is your name? ")
while True:
  try:
    age = int(input("How old are you? "))
    break
  except ValueError:
    print("Please enter a valid age")


print('\nPerfect.')
print(f'Nice to meet you {name}.\n{age}, my lucky number!')
print('\nLet\'s get this account set up for you!\nPlease select one of the following')
print('*It is recommneded to go in sequential order*')


#Displaying conversation options for the user function
def display_menu():
  print('\n1. Account type')
  print('2. Generate an Account number')
  print('3. Security Questions')
  print('4. Need help deciding on account type?')
  print('5. Exit')

#User selection function
def user_selection():
  while True:
    try:
      selection = int(input("What would you like to do? (Put option number): "))
      break
    except ValueError:
      print("Please enter a number")
  
  if selection == 1:
    print("account type")
  elif selection == 2:
    print("generate an account number")
  elif selection == 3:
    print("security questions")
  elif selection == 4:
    print("need help deciding on account type?")
  elif selection == 5:
    global in_use
    in_use = False
    print("Exiting the chatbot, goodbye! :)")
    sys.exit(0)
  else:
    print("Invalid Input, try again\n")
    user_selection()

user_selection()