# Write a program to input eight numbers from the user and display all the unique numbers (once).

s=set()

a=int(input("Enter 1st number :"))
s.add(a)

b=int(input("Enter 2nd number :"))
s.add(b)

c=int(input("Enter 3rd number :"))
s.add(c)

d=int(input("Enter 4th number :"))
s.add(d)

e=int(input("Enter 5th number :"))
s.add(e)

f=int(input("Enter 6th number :"))
s.add(f)

g=int(input("Enter 7th number :"))
s.add(g)

h=int(input("Enter 8th number :"))
s.add(h)

print(s)




# Can we have a set with 18 (int) and '18' (str) as a value in it?

p={19,'19'}
p.add(19.0) # If int and float number are same it get removed but if in string same number is given it is printed 
print(p)
# Note: Sets do not contain list inside it whereas we can use tuple inside it.