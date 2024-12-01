# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):

    if a>b and a>c :
        print(f"{a} is the gratest number.")

    if b>a and b>c :
        print(f"{b} is the gratest number.")

    else:
        print(f"{c} is the greatest number.")

greatest(12,45,2)

