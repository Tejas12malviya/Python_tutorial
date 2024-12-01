# Write a program to print multiplication table of n using for loops in reversed order.

n=int(input("Enter the number whose table you want :"))

print(f"The Table of {n} is :-")

for i in range(1,11):
    print(f"{n}*{i} = ",n*i)