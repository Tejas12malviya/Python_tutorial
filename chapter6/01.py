# Write a program to print multiplication table of a given number using for loop.

a=int(input("Enter the number :"))
print(f"The multiplication table of {a} is :")

for i in range(1,11):
    print(f"{a}*{i} = {a*i}")

# -----------------OR--------------------
# Multiplication table using while loop

i=1
while i<11:
    print(f"{a}*{i} = {a*i}")
    i+=1