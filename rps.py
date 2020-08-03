#pick random from rock, paper or scissors
#ask user to enter rock paper or scissors
#check the rules of rps to see who wins and print the result
#keep counters for the score

import random
import time

choices=["rock","paper","scissors"]

userInputCorrect = False


while not userInputCorrect:
    player1=input("Rock Paper or Scissors?\n")
    if player1 in choices:
        userInputCorrect = True
        print ("you chose " + player1)
        time.sleep(1)
    else:
        print("oops :( ")
    

player2=random.choice(choices)

print("opponent chose " + player2 )
time.sleep(1)


if player1 == "rock":
    if player2 == "rock":
        print("draw")
    elif player2 == "paper":
        print("player2 wins")
    elif player2 == "scissors":
        print("player1 wins")

        
if player1=="scissors" :
    if player2=="scissors":
        print("draw")
    elif player2 == "rock":
        print("player2 wins")
    elif player2== "paper":
        print("player1 wins")

    
if player1 == "paper":
    if player2 =="paper":
        print("draw")
    elif player2== "rock":
        print("player1 wins")
    elif player2=="scissors":
        print("player2 wins")
