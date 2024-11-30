# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

a=int(input("Enter the score of Physics :"))
b=int(input("Enter the score of Chemistry :"))
c=int(input("Enter the score of Maths :"))

total_percentage=(a+b+c)/3

if (a>33 and b>33 and c>33):
    if (total_percentage>40):
        print("You are Pass.",total_percentage)

else:
    print("You are Fail.",total_percentage)