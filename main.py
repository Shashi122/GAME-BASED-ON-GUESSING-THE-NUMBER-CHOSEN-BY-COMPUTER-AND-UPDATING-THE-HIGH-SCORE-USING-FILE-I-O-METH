##PROJECT 2

import random

randnumber=random.randint(1,100)
userguess=None
guesses=0

while(userguess!=randnumber):
    userguess=int(input("enter your guess"))
    guesses+=1
    
    if(userguess==randnumber):
        print("you guessed it right")
        
    else:
        if(userguess>randnumber):
            print("you guessed it wrong please enter a smaller number")
        else:
            print("you guessed it wrong please enter a larger number")
            
print("you guessed it in ",guesses," guesses")

with open("hscore.txt") as f:
    hs=int(f.read())
    
if guesses<hs:
    print("you have broken the high score")
    with open("hscore.txt","w") as f:
        f.write(str(guesses))
        