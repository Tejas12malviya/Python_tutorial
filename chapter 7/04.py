# Write a recursive function to calculate the sum of first n natural numbers.


def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)

result= sum(10)
print("Sum of first 10 natural numbers are :",result)




# Write a python function to print first n lines of the following pattern:
# ***
# **   - for n = 3
# *


def pattern(n):
    for i in range (n):
        print("*"*(n-i))

pattern(3)
