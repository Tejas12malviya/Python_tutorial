# Write a python program using function to convert Fahrenheit to Celsius .

def far_to_celcius(far):
    celcius=(far-32)*(5/9)
    print(f"{far}°F is equal to {celcius:.2f}°C")
    # return celcius

far_to_celcius(200)


# prevent a python print() function to print a new line at the end.

print("Hello",end="-")
print("World")
