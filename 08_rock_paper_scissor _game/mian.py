# THIS IS SIMPLE ROCK PAPER SCISSOR GAME SO ENJOY

import random 
choices = [ "rock", "paper", "scissor"]
guess = 0
count_win = 0

while True:
    guess = input("enter your choice :     ")
    computer = random.choice(choices)
    print("computer chose:", computer)
    
    if guess == computer:
          print("tie")
    
    elif (guess == "rock" and computer == "scissor") or \
         (guess == "scissor" and computer == "paper") or \
         (guess == "paper" and computer == "rock"):
        
        
        print("you win")   
        count_win += 1
         
    else:
         print("you lose")             

