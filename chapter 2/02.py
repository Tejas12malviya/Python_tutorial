# Write a program to detect double space in a string

a=("Hi I  am learning  Python")
print(a.find("  "))
# Gives -1 if there is no double space

# Replace the double space from problem 3 with single spaces.

print(a.replace("  "," "))