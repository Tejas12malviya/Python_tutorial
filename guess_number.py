# ----------------------------------------NUMBER GUESSING GAME---------------------------------------

import random 

randnum= random.randint(1,100)

while True:
    userChoice=(input("Guess the number or Quit(Q): "))
    if(userChoice=='Q'):
        break

    userChoice=int(userChoice)
    if(userChoice == randnum):
        print("Success! You guess the number.")
        break
    elif(userChoice<randnum):
        print("your choice was too small. Take a bigger Guess...")
    else:
        print("your choice was too big. Take a smaller Guess...")
        

print("--------GAME OVER-------")
    
