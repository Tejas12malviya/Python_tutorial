# Write a program to calculate the factorial of a given number using for loop.

f=int(input("Enter the number whose factorial you want :"))

result=1
for i in range(1,f+1):
    result=result*i
    

print(f"Factorial of {f} is :",result)