#alphabet_speed
import time

choice = input("Please input READY, all in caps when you want to start!: ")
if choice == "READY":
    startTime = time.time()
    print("This is the time right now:",startTime )
    abcd = input("Now input the alphabet! (No spaces!) : ")
    endTime = time.time()
    print("This is the time right now:",endTime )
    if abcd == "abcdefghijklmnopqrstuvwxyz":
        
        print("You got it all correct! Your time is:", startTime - endTime)
    else:
        print("Your IQ = -100 XD")
else:
    print("Bye then")
    
    
   