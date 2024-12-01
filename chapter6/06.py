# Write a program to print the following star pattern: 
# *
# **
# *** for n = 3

n=3

for i in range (1,n+1):
    print("*"*i)


# ---------------------------PATTERN 2--------------------------------
    


# Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3


n=3

for i in range(1,n+1):
    print((n-i)*" ","*"*(2*i-1))




# ---------------------------PATTERN 3--------------------------------

# Write a program to print the following star pattern.
# * * *
# *   *   for n = 3
# * * *

n=3

for i in range(n):
    print("*",end=" ")
print()

for i in range(n-2):
    print("*",end=" ")
    for j in range(n-2):
        print(" ",end=" ")
    print("*")

for i in range(n):
    print("*",end=" ")
print()