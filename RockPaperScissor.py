import random

state = ["rock", "paper", "scissors"]

#take the input from the user to specify how many round will be played
round = int(input("How many round do you want?:"))
score_1=0
score_2=0
count=1

#Write a while loop and put the game inside
while True:
    #Select a random action for each player for every loop
    player_1 = random.choice(state)
    player_2 = random.choice(state)

    #Set the scores of players to 0 (the tie condition)
    if(player_1==state[0] and player_2==state[0]) or (player_1==state[1] and player_2==state[1]) or (player_1==state[2] and player_2==state[2]):
        score_1 = score_1
        score_2 = score_2

    #Create a list containing the three actions of the game.
    if(player_1==state[0] and player_2==state[2]) or (player_1==state[1] and player_2==state[0]) or (player_1==state[2] and player_2==state[1]):
            score_1 += 1
            score_2 = score_2
    if(player_2==state[0] and player_1==state[2]) or (player_2==state[1] and player_1==state[0]) or (player_2==state[2] and player_1==state[1]):
        score_2 += 1
        score_1 = score_1
    #Print the players choices
    print("Round",count,"-> Player1:",player_1,"- Player2:",player_2)
    print("\tScore of the player1:",score_1,"\n\tScore of the player2:",score_2)
    count+=1
  
    #Stop the while loop if the count equals the number of rounds
    if (score_1 == round or score_2 ==round):
        break

#Print the outcome of the game
print("-------------------------------")
print("Score of the player1:",score_1,"\nScore of the player2:",score_2)
