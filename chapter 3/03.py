#   Write a program to sum a list with 4 numbers.

l1=[]

a=int(input("Enter 1st number :"))
l1.append(a)

b=int(input("Enter 2nd number :"))
l1.append(b)

c=int(input("Enter 3rd number :"))
l1.append(c)

d=int(input("Enter 4th number :"))
l1.append(d)

print(f"Sum of Given four numbers are :{sum(l1)}")



# Write a program to count the number of zeros in the following tuple:

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))