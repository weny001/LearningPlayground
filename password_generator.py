#Generate Password
import random

choice = input("Would you like a random password to be generated? Y/N: ")
if choice == "Y":
    uppercaseLetter1 = chr(random.randint(65,90))
    uppercaseLetter2 = chr(random.randint(65,90))
    lowercaseLetter1 = chr(random.randint(97,122))
    lowercaseLetter2 = chr(random.randint(97,122))
    digit1 = chr(random.randint(48,57))
    digit2 = chr(random.randint(48,57))
    punctuationSign1 = chr(random.randint(33,152))
    punctuationSign2 = chr(random.randint(33,152))
    
    gen_pass = [ uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2 ]
    
    random.shuffle(uppercaseLetter1, punctuationSign2)
    
    print(gen_pass)

    
else:
    print("Go away then :p")

