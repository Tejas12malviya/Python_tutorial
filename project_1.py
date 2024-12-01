# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.
import random

print("We are playing Snake, Water, Gun Game \nSnake='s' \nWater='w'\nGun='g")
computer=random.choice([1,2,3])
yourCall=input("Enter your choise: ")
yourDict={'s':1,'w':2,'g':3}
reverseDict={1:'Snake',2:'Water',3:'Gun'}

you=yourDict[yourCall]
 
print(f"Your choice: {reverseDict[you]}\nComputer Choice: {reverseDict[computer]}")

if computer==you:
    print("It's Draw.")

else:
    if computer==1 and you==3:
        print("You Won.")

    elif computer==2 and you==1:
        print("You Won.")

    elif computer==3 and you==2:
        print("You Won.")

    else:
        print("You Loose.")    

