from AREA.area import *
class Reactangle(Area):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return (f"Area of rectangle with {self.length} length and {self.breadth} breadth is {self.length*self.breadth}")
