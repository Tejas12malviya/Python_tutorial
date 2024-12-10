# static methods
# It do not contain self parameter and works at class level not on object level

class Student:
    @staticmethod   # It is called decorator
    def college():
        print("ABC College")

Student.college()


# -----------------------------------SUPER METHOD------------------------------------------
# parent class se direct atrribute ko call karne par we get error so, we use super class for it , example

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car is started.")

class Toyota(Car):
    def __init__(self,color, type):
        self.color=color
        super().__init__(type) # By using these super method we can call attribute (type) from parent class (Car)
        super().start()

car1=Toyota("Red","Petrol")
print(car1.type)



# --------------------------------------------CLASS METHOD----------------------------------------
# uses @classmethod decorator

class Car:
    name="Fortuiner"

    def changename(self,name):
        self.name=name 

c1=Car()
c1.changename("Range Rover")
print(c1.name) 
print(Car.name)   # It means self.name=name is not updating the previous name present inside the class , it makes new instance
# where as if we use @classmethod decorator it updates our instance not make new one.
 
        
class Car:
    name="Fortuiner"

    @classmethod
    def changename(cls,name):
        cls.name=name

car1=Car()
car1.changename("Range Rover")
print(car1.name)
print(Car.name)

# NOTE : static method is generally used when we have to give no attribute to that function,
#        instance method(__init__) is used when we have to give 'self' command
#        class method is used when we have to give 'cls' command


# ----------------------------------PROPERTY DECORATOR-----------------------------------------

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        self.percentage=str((self.chem + self.math + self.phy)/3)  + "%"

stud1=Student(96,84,78)
print(stud1.percentage)

stud1.math=90
print(stud1.math)
print(stud1.percentage)
# It can update the individual scores of each subject but can not update the overall percentage
# It can be done by using @property decorator
# @property decorator converts the given function as attribute, example



class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    
    @property
    def percentage(self):
        percentage=str((self.chem + self.math + self.phy)/3)  + "%"
        return percentage

stud1=Student(96,84,78)
print(stud1.percentage)

stud1.math=93
print(stud1.math)
print(stud1.percentage) # shows latest percentage 

