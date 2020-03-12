import random
numGuess = 0
numPlay = 0
numComp = random.randint(1,1000)
print(numComp)
while numPlay != numComp:
    numPlay = int(input("Please guess the number!: "))
    numGuess = numGuess + 1 
    if numPlay == numComp:
        print("You have guessed the right number! It was",numComp)
    else:
        print("That's not right!")
        