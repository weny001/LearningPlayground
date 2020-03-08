#random deck puller

import random
cardNum = random.randint(1,10)
houseList = ["Spades", "Clubs", "Hearts", "Diamonds"]
picList = ["King", "Queen", "Jack"]
cardHouse = random.choice(houseList)

choice = input("Do you want to draw a random card? Y/N: ")
if choice == "Y":
    if cardNum == 10:
        picCard= random.choice(picList)
        print(picCard, "of" , cardHouse)
    elif cardNum == 1:
        print("Ace of", cardHouse)
    else:
        print(cardNum ,"of" ,cardHouse)
else:
    print("Go away :)")
