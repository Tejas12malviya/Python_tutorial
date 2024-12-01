# Function defination

def goodDay(name,end):
    print("Good Day, "+name)
    print(end)

# function Call 
goodDay("Rohan","Thank You")
goodDay("Ram","Thanks")
goodDay("Shivam","Namaste")


# Return value concept
def avg():
    a=int(input("Enter your number: "))
    b=int(input("Enter your number: "))
    c=int(input("Enter your number: "))

    average=(a+b+c)/3
    return average

def sum():
    a=int(input("Enter your number: "))
    b=int(input("Enter your number: "))
    c=int(input("Enter your number: "))

    sum=(a+b+c)
    print(sum) 

a=avg()
print(a)

sum()
# print ka use function ke andar hi karna padta aur vo predefined hota hai but return use karne par ham use dusre varible ko assign kavakar print karte hai.

# default value parameter.

def name(name,ending='Thank you'):
    print('Good Morning',name)
    print(ending)

name('Tejas',"Thanks")
name("Sohan")