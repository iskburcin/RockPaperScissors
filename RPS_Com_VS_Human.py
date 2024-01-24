#Import the random library
import random

#create a list containing the three actions of the game.
actions = ['rock','paper','scissors']

#Set the scores of players to 0
score_of_computer = 0
score_of_user = 0
#Ask the user how many rounds they want to play
rounds = input('How many round you are going to play: ')

#Add a round_counter that is 0 at the beginning
round_counter = 0

#Write a while loop and put the game inside
while(True):
  #Increase round_counter by and print it
  round_counter += 1

  #Select a random action for computer
  coumputer = random.choice(actions)
  #Ask player to choose an action
  user = input('Enter your action: ')

  #Print the players choices
  print(f'Round {round_counter} -> Computer: {coumputer}\tUser: {user}')

  #tie condition
  if(coumputer==user):
    score_of_user = score_of_user
    score_of_computer = score_of_computer

  #Remaining conditions
  elif(coumputer=='rock'):
    if user == 'paper':
      score_of_user += 1
    elif user == 'scissors':
      score_of_computer += 1

  elif coumputer == 'paper':
    if user == 'scissors':
      score_of_user += 1
    elif user == 'rock':
      score_of_computer += 1

  elif(coumputer=='scissors'):
    if user == 'rock':
      score_of_user += 1
    elif user == 'paper':
      score_of_computer += 1
  print(f'\t   Computer:{score_of_computer}\t\tUser: {score_of_user}')
  #Stop the while loop if the round_counter equals the number of total rounds
  
  if(round_counter == int(rounds)):
    break

#Print the outcome of the game by using conditional statements
print('------------------------------------------')
print(f'The Final Score {score_of_computer}:{score_of_user}')
