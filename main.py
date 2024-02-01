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
global age
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
  print('4. Account Summary (Run when finished setting up account)')
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
    account_type()
  elif selection == 2:
    generate_acc_num()
  elif selection == 3:
    sec_quest()
  elif selection == 4:
    acc_summary()
  elif selection == 5:
    global in_use
    in_use = False
    print("Exiting the chatbot, goodbye! :)")
    sys.exit(0)
  else:
    print("Invalid Input, try again\n")
    user_selection()


def account_type():
  global acc_type
  acc_type = input("Savings, Checking, Parent Joint, or Student?: ")
  display_menu()
  user_selection()


def generate_acc_num():
  global acc_num
  acc_num = random.randint(1000, 9999)
  print(f'\n*Your account number is {acc_num}*')
  display_menu()
  user_selection()

def sec_quest():
  print("Answer these security questions")
  global store_answer
  store_answer = []
  sec_q1 = input("What is your favorite color? ")
  sec_q2 = input("What is your favorite food? ")
  store_answer.append(sec_q1)
  store_answer.append(sec_q2)
  print(f'Your answers are {store_answer}')
  display_menu()
  user_selection()

def acc_summary():
  print(f'\n*Account Summary*\nName: {name}\nAge: {age}')
  print(f'Account Type: {acc_type}\nAccount Number: {acc_num}')
  print(f'Security Questions Answers: {store_answer}')
  sys.exit(0)

display_menu()
user_selection()