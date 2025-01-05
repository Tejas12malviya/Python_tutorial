print("Hello")
'''String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.'''

day=int(input('Enter number of days remaining for yor birthday:'))

print(f"You have {int(day/7)} weeks and {day%7} days left for your birthday.")


mylist=[10,20,30,'Hii']
print(mylist)
print(mylist.count(20))

mylist.append(40)  # insert given element at last of the list.
print(mylist)

mylist.insert(3,25)  # insert the given element on 3rd index i.e., after 3 elements.
print(mylist)

mylist.pop(4)  # delete the element present on 4th index. whereas remove deletes that element which is called.
mylist.insert(4,'Harry')
mylist.remove("Harry")

mylist.sort(reverse=True)
print(mylist)

print(mylist[0:5:2])  # ending index is excluded

#---------------------------------------SET-----------------------------------------------

# sets do not contains indexing
marks={10,10,20,30,40,70,70,20,100,50,40}
print(marks)

marks.discard(20)
print(marks)

marks.add(15)

# -----------------------------------------------------------------------------------------

class AnimalList:
    def __init__(self,animals=None):
        self.animals=animals if animals else []

    def add_animal(self,animal):
        self.animals.append(animal)

    def display_animals(self):
        print("Animals :",self.animals)


my_animals = AnimalList()

while True:
    print("\nMenu:")
    print("1. Add an animal")
    print("2. Display animals")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        animal = input("Enter the name of the animal to add: ")
        my_animals.add_animal(animal)
        print(f"{animal} has been added.")
    elif choice == "2":
        my_animals.display_animals()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
