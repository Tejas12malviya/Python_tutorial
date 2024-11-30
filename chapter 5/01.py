# Write a program to find the greatest of four numbers entered by the user.

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
d=int(input("Enter the fourth number :"))
 
if (a>d) :
    if (a>c):
        if (a>b):
            print(f"{a} is the greatest number")      
        else:
            print(f"{b} is the greatest number") 

    elif(c>a):
        if (c>b):   
            print(f"{c} is the greatest number")
        else:
            print(f"{b} is the greatest number") 

else:
    print(f"{d} is the greatest number")


# -------------------OR--------------------


a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=int(input("Enter the third number :"))
d=int(input("Enter the fourth number :"))

print(max(a,b,c,d))