
import random
# ------------------------------------------------------------------------------------
print("-----------------Let's do some calculations-----------------")
print("What do you want to do?\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
choice=input(": ")
if choice!=('4'and'5'):
    print('Choose your range\n 1.1-50\n 2.1-100')
    range=input(': ')

if range=='1':

    num1=random.randint(1,51)
    print("Your First number is:",num1)
    num2=random.randint(1,51)
    print('Your Second number is:',num2)

    if choice=='1':
        while True:
            ans=int(input('Enter the sum of the two numbers: '))
            if ans!=(num1+num2):
                print('Try again')
            else:
                print('You got it right')
                break
    
    if choice=='2':
        while True:
            ans=int(input('Enter the difference of the two numbers: '))
            if ans!=(num1-num2):
                print('Try again')
            else:
                print('You got it right')
                break

    if choice=='3': 
        while True:
            ans=int(input('Enter the product of the two numbers: '))
            if ans!=(num1*num2):
                print('Try again')
            else:
                print('You got it right')
                break

if range=='2':

    num1=random.randint(1,101)
    print("Your First number is:",num1)
    num2=random.randint(1,101)
    print('Your Second number is:',num2)

    if choice=='1':
        while True:
            ans=int(input('Enter the sum of the two numbers: '))
            if ans!=(num1+num2):
                print('Try again')
            else:
                print('You got it right')
                break
    
    if choice=='2':
        while True:
            ans=int(input('Enter the difference of the two numbers: '))
            if ans!=(num1-num2):
                print('Try again')
            else:
                print('You got it right')
                break

    if choice=='3': 
        while True:
            ans=int(input('Enter the product of the two numbers: '))
            if ans!=(num1*num2):
                print('Try again')
            else:
                print('You got it right')
                break

if choice=='4':
    num2=random.randint(1,21)
    num=random.randint(1,101)
    num1=num2*num
    print("Your First number is:",num1)
    print('Your Second number is:',num2)

    while True:
        ans=int(input('Enter the quotient of the two numbers: '))
        if ans!=(num1/num2):
            print('Try again')
        else:
            print('You got it right')
            break

if choice=='5':
    print('Thank you for playing')
    exit()
