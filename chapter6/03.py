# Write a program to find whether a given number is prime or not.

num=int(input("Enter the number :"))

for i in range(num-1,1,-1):
    if (num%i==0):
        print(f"{num} is the composite number.")
        break

else:
    print(f"{num} is the prime number.")
        