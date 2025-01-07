from AREA.area import *

class Circle(Area):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return(f"Area of circle with {self.radius} radius is {3.14*(self.radius**2)}")

