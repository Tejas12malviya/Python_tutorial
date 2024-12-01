# Write a python function which converts inches to cms.
def inch_to_cm(n):
    cm=n*2.54
    print(f"{n} inches is equal to {cm:.2f} centimeters.")

inch_to_cm(12)


# Write a python function to print multiplication table of a given number.

def table(n):
    for i in range(1,11):
        print(f"{n}*{i} = ",n*i)

print("Multiplication table of given number is :")
table(8)