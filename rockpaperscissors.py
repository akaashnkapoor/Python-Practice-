#A Rock-Paper-Scissors Game but with a CPU instead of a two player game. 
#Made by: Akaash Kapoor
#Date: September 29th 2019
import random

print("WELCOME TO THE GAME OF ROCK PAPER SCISSORS!\n") 
options = ['rock', 'paper', 'scissors'] #Available options stored in a string list. 

while True: #Infinite loop is implemented in case player wants to play again

    userChoice = input("Choose your option (type in lower case): ") #Getting user input on the three choices.
    while userChoice != 'rock' and userChoice != 'paper' and  userChoice != 'scissors': #Validating if user input is appropriate.
        userChoice = input("Choose a valid option: ")

    cpuChoice = random.choice(options) #CPU picks one of the options
    print("CPU picked: ", cpuChoice) #Display's CPU's choice

    #The possible outcomes formulated through if-elif statements. 
    if userChoice == 'rock' and cpuChoice == 'scissors':
        print("YOU WIN! CONGRADULATIONS!")
    elif userChoice == 'paper' and cpuChoice == 'rock':
        print("YOU WIN! CONGRADULATIONS!")
    elif userChoice == 'scissors' and cpuChoice == 'paper':
        print("YOU WIN! CONGRADULATIONS!")
    elif userChoice == cpuChoice:
        print("ITS A DRAW!")
    elif userChoice == 'rock' and cpuChoice == 'paper':
        print("YOU LOSE! BETTER LUCK NEXT TIME!")
    elif userChoice == 'paper' and cpuChoice == 'scissors':
        print("YOU LOSE! BETTER LUCK NEXT TIME!")
    elif userChoice == 'scissors' and cpuChoice == 'rock':
        print("YOU LOSE! BETTER LUCK NEXT TIME!")

    #Getting user input to play again
    userInput = input("Play again? Type 'yes' or 'no': ")
    while userInput != 'yes' and userInput != 'no': #Validating user input once again. 
        userInput = input("Choose a valid option: ")

    #If user types no, break out of the loop and terminate program, otherwise continue the program through the infinite loop. 
    if userInput == 'no':
        break

    
print("Exiting Game...")

