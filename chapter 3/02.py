# Write a program to accept marks of 6 students and display them in a sorted manner.

Student=[]

s1=input("Enter 1st  Student's name :")
Student.append(s1)

s2=input("Enter 2nd  Student's name :")
Student.append(s2)

s3=input("Enter 3rd  Student's name :")
Student.append(s3)

s4=input("Enter 4th  Student's name :")
Student.append(s4)

s5=input("Enter 5th  Student's name :")
Student.append(s5)

s6=input("Enter 6th  Student's name :")
Student.append(s6)

Student.sort()
print(Student)

# Note: List are mutable i.e. changes can be done directly on it whereas tuples are immutable.

# Check that a tuple type cannot be changed in python.

t1=("Apple",)
l1=["Apple"]

print(type(t1))
print(type(l1))

t2=("Banana",)
l2=["Banana"]

l1[0]=l2
print(l1)

l1.append(l2)
print(l1)

# print(t1+t2)
try:
    t1[0]=t2
except TypeError as e:
    print(f'Error:{e}')  
