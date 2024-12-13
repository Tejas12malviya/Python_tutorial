# --------------------------------PHONE NUMBER GENRATOR WITH CODE--------------------------
import random
import string

mobile_number='9399'
for i in range (6):
    mobile_number += random.choice(string.digits)

print("Your new mobile number is: ",mobile_number)
