# Find the avg marks of a student using the classes

class Student:
    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def get_avg(self):
        total = 0
        for mark in self.marks:
            total += mark
        print(f"hi, {self.name} your avg marks is: {total/3:.2f}")

s1 = Student("surya", [98, 97, 86, 86, 64])
s1.get_avg()