# Average marks of 3 subject for given student

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for values in self.marks:
            sum += values
        print(f"Hii {self.name}, your avg score is: {sum/3}")

s1=Student("Rohan",[99,95,85])
s1.get_avg()

        