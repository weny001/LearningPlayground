import random
import time
choice = 0 
startNum = random.randint(20,30)
print("The starting number is:",startNum)

while startNum>0:
    playC = int(input("How many do you want to remove?: "))
    if playC >3:
        print("Please input a number lower or equal to 3.")
    elif playC <=0:
        print("Enter a positive number! Not 0 either.")
    else:
        startNum = startNum - playC
        print(startNum,"left")
        if startNum == 0:
            print("Game has finished")
            print("You lost")
            break
        
        if startNum == 3:
            compC = 2
            startNum = startNum - compC
            print("Computer removes", compC)
            print(startNum,"left")
        elif startNum == 2:
            compC = 1
            startNum = startNum - compC
            print("Computer removes", compC)
            print(startNum,"left")
        elif startNum == 1:
            compC = 1
            startNum = startNum - compC
            print("Computer removes", compC)
            print(startNum, "left")
            print("You have won")
            
        else:
            compC = random.randint(1,3)
            print("Computer removes", compC)
            startNum = startNum - compC
            print(startNum,"left")
    
