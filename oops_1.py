# Creating class
class Student:
    name= "Rohan kumar"

# Creating object(instance)
s1=Student()
print(s1.name)

# Constructor
# It is a special function which is invoke while object creation.

class Stud:
    #  default/empty constructor, if we didn't give it is automatically called.
    def __init__(self):
        pass

    # parameterised constructor
    def __init__(self,fname,marks):# data stored inside the class or inside the function is called attributes.
        self.fname=fname
        self.marks=marks
        print(f"My name is {fname} and I got {marks} marks.")

Stud("Sohan",56)# here that construtor will be called whose parameter matches. 

# Class is the collection of dat(attribute) and methods(like functions)
