#blackJack
import random

ace = 11
king = 10
queen = 10
jack = 10
playScore = 0
valid=1
valid=2
valid=3
picCard = ["king", "queen", "jack"]

print("Welcome to the menu! Please type in the corresponding number to select that option")
print("1. Play Game")
print("2. Instructions")
print("3. Quit")

while valid>1:
    valid=int(input("Enter the number: "))
    if valid==1:
        print("Get ready to play!")
        playerCard1 = random.randint(1,11)
        playerCard2 = random.randint(1,11)
        
        playScore = playerCard1 + playerCard2
        print("Your score is:",playScore)
        while playScore<21:
            
            playChoice = input("Would you like to hit, or stand?: ")
            if playChoice == "hit":
                playerCard3 = random.randint(1,11)
                print("Your new card is", playerCard3)
                playScore = playerCard3 + playScore
                print("Your score is:", playScore)
                if playScore == 21:
                    print("You hit blackjack!")
                    compCard1 = random.randint(1,11)
                    compCard2 = random.randint(1,11)
                    compScore = compCard1 + compCard2
                    print("Computer score is:", compScore)
                    if compScore<=18:
                        compCard3 = random.randint(1,11)
                        compScore = compCard3 + compScore
                        print("Computer final score:", compScore)
                        if compScore>21:
                            print("Computer is bust!")
                        
                    
                    
                elif playScore > 21:
                    print("You are bust!")
                    print("Your final score was:", playScore)
                    compCard1 = random.randint(1,11)
                    compCard2 = random.randint(1,11)
                    compScore = compCard1 + compCard2
                    print("Computer score is:", compScore)
                    if compScore<=16:
                        compCard3 = random.randint(1,11)
                        compScore = compCard3 + compScore
                        print("Computer final score:", compScore)
                        break
                    
            elif playChoice == "stand":
                print("Your score is:", playScore)
                
                compCard1 = random.randint(1,11)
                compCard2 = random.randint(1,11)
                compScore = compCard1 + compCard2
                print("Computer score is:", compScore)
                if compScore<=16:
                    compCard3 = random.randint(1,11)
                    compScore = compCard3 + compScore
                    print("Computer final score:", compScore)
                    if compScore == 21:
                        print("Computer hits blackjack!")
                    elif compScore>21:
                        print("Computer is bust!")
                    break
                
            
        
        
            
            
        
        
        
    
    elif valid==2:
        print("How to play blackjack:")
        print("The aim of this game is to get as close to the number 21, when you want to add another card, type in hit, if you are satisfied with your score, type in stand. Picture card are worth 10 points and Ace can be worth 1 or 11 points.")
    
    elif valid==3:
        print("Let's go!")
        
    else:
        print("1. Play Game")
        print("2. Instructions")
        print("3. Quit")
