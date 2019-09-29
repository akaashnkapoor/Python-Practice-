#The palindrome code. Determines if a letter is a palindrome. 

word = input("Please enter a word: ") #Getting user input.
duplicate = word[::-1] #Reverses the order of the letters but places it in another string variable.
counter = 0 #Counter to keep track of the letters in duplicate. 

for letterWord in word:
    if letterWord is duplicate[counter]: #If the two letters are the same in that iteration, increase counter by 1.
        counter = counter + 1
    else:
        print("This word is not a palindrome")
        quit() #This function terminates the program. 
    
print("This word is a palindrome")

    




