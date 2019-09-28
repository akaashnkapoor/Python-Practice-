#Comparing Two Random Lists in Python
#Written by Akaash Kapoor
#Date: Sept 28th 2019

import random

while True: #Put into an infinite loop to prevent an unexceptable value from being entered. 
    numMax = int(input("Enter the max number of the two lists: ")) #Includes user unput for both lists. Compatible with negative numbers.
    numMin = int(input("Enter the min number of the two lists: "))
    numList = int(input("Enter the capacity of the two lists: "))

    if numMax < numMin or numList <= 0:
        print("Please input acceptable values\n") #Runs through the infinite loop again.
    else:
        break #Breaks out of the infinite loop. 


a = random.sample(range(numMin,numMax), random.randint(1,numList)) #Ramdomly generates a list of numbers.
b = random.sample(range(numMin,numMax), random.randint(1,numList)) #Values range from 0 to 100.
finallist = []

print("List a is: ", a) #Prints out the random list for a.
print("List b is: ", b) #Prints out the random list for b.

a = set(a) #Removes any duplicate values in list a

for x in a: #x is a temp variable. Switches values through the loop.
    for y in b: #y is a temp variable as well.
        if x == y: #If the value of x is equal to y, append the value to final list. 
            finallist.append(x)
            break #Breaks out of the inner loop.
        


print("The final list is: ", finallist)



