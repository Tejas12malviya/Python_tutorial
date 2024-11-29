# Write a python program to display a user entered name followed by Good Afternoon using input () function.
from datetime import datetime

# Get current datetime
current_time = datetime.now().hour

# Print current datetime
# print("Current Time:", current_time)

name=input("Enter your name :")

if 5 <= current_time <12:
    print("Good Morning!",name)
elif 12 <= current_time<17:
    print("Good Afternoon!",name) 
elif 17 <= current_time<21:
    print("Good evening!",name) 
else :
    print("Good Night!")       

