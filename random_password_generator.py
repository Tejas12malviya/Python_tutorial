# -----------------------------------NUMBER PASSWORD GENERATE------------------------------

import random
import string

num_pass_len=int(input("Enter the number of digit password you want: "))
numValue=string.digits

password=''
for i in range(num_pass_len):
    password += random.choice(numValue)

print("Your random password is: ",password)

# --------------------------------------PASSWORD GENERATION--------------------------------

pass_len=int(input("Enter the password length you want: "))
numValue=string.digits+ string.ascii_letters+ string.punctuation

password=''
for i in range(pass_len):
    password += random.choice(numValue)

print("Your random password is: ",password)