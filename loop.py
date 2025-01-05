# Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#
# - Create a while loop that prints all elements of the my_list variable 3 times.
#
# - When printing the elements, use a for loop to print the elements
#
# - However, if the element of the for loop is equal to Monday, continue without printing

i=0
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

while i <3:
    for x in my_list:
        if x=='Monday':
            continue
        print(x)
    print('-----')
    i+=1