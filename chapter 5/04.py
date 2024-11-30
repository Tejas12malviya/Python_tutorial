# Write a program which finds out whether a given name is present in a list or not.

l1=["Rashik","Deepak","Buke","Kratika","Shivani","Rai","Yogita"]

a=input("Enter the name :")

if a in l1:
    print("Your name is in the given list.")

else:
    print("Your name is not present in the list.")




# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

a=float(input("Enter your Percentage : "))

if a>90 and a<=100 :
    print(f"Your Grade is Ex and you got {a} Percentage.")

elif a>80 and a<=90 :
    print(f"Your Grade is A and you got {a} Percentage.")

if a>70 and a<=80 :
    print(f"Your Grade is B and you got {a} Percentage.")

if a>60 and a<=70 :
    print(f"Your Grade is C and you got {a} Percentage.")

if a>50 and a<=60 :
    print(f"Your Grade is D and you got {a} Percentage.")

if a<=50 :
    print(f"Your Grade is F and you got {a} Percentage.")

else:
    print("Wrong Input")




# Write a program to find out whether a given post is talking about "Rohan" or not.'

post=input("Enter the post :")

if ("Rohan".lower() in post.lower()):
    print("Post is talking about Rohan.")

else:
    print("Post is not talking about Rohan.")