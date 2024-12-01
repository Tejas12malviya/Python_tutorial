# Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter the number :"))

s=[]
i=1
while i<n+1:
    s.append(i)
    i+=1
# print(s)

print(f"Sum of First {n} natural number is :",sum(s))