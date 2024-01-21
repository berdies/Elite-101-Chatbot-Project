# Elite 101 Chatbot
#Importing necessary libraries
import random
import sys

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

display_menu()

selection = input("What would you like to do? (Put option number) ")