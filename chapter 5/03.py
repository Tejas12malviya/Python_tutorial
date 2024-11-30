# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

s1="Make a lot of money"
s2="buy now"
s3="subscribe this"
s4="click this"

Message=input("Enter the commrnt :")

if ((Message==s1)or(Message==s2)or(Message==s3)or(Message==s4)):
    print("Message is Spam.")

else:
    print("Message is not Spam.")





# Write a program to find whether a given username contains less than 10 characters or not.

a=input("Enter the username :")

if len(a)<10:
    print("Username is than 10 characters.")

elif len(a)==10:
    print("Username satisfied.")

else:
    print("Username is greater than 10 characters.")