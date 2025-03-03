# Positional Vs Keyword Arguments

def my_func(a,b,/):   # here my_func is taking positional arguments
    print (a+b)

def my_func1(*,a,b):  # here my_func1 is taking keyword arguments
    print (a+b)

my_func(10,20)      
# my_func(a=10,b=20)  # this will give error because my_func is taking positional arguments

my_func1(a=10,b=20)
# my_func1(10,20)     # this will give error because my_func1 is taking keyword arguments