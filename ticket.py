# Train ticket problem

from random import randint

class train :

    def __init__(self,TrainNO):
        self.trainNO=TrainNO

    def book(self,fro,to):
        print(f"Ticket is booked in Train no. {self.trainNO} from {fro} to {to}.")

    def get_status(self):
        print(f"Your train with Train no. {self.trainNO} is running on Time.")

    def Fair(self,fro,to):
        print(f"Ticket fair of Train no. {self.trainNO} going from {fro} to {to} in general coach is rupees {randint(100,300)}")
        print(f"Ticket fair of Train no. {self.trainNO} going from {fro} to {to} in sleeper coach is rupees {randint(500,900)}")
        print(f"Ticket fair of Train no. {self.trainNO} going from {fro} to {to} in A.C. coach is rupees {randint(1200,2000)}")

t=train(12599)
t.book("Nagpur","Hyderabad")
t.get_status()
t.Fair("Nagpur","Hyderabad")

# --------------------------------------------------------------------------------------------------------------------------------

# Calculator

class number:

    def __init__(self,x):
        self.x=x
    def square(self):
        print(f"The square of {self.x} is {self.x*self.x}")
    def cube(self):
        print(f"The cube of {self.x} is {self.x*self.x*self.x}")
    def square_root(self):
        print(f"The square_root of {self.x} is {self.x**(1/2):.2f}")
    def cube_root(self):
        print(f"The square of {self.x} is {self.x**(1/3):.2f}")

a=number(64)
a.square()
a.cube()
a.square_root()
a.cube_root()
