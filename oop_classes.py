# OOP - Object Oriented Programming for Beginners
# -------------------------------------------------------
class Student:

    name = 'surya'
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Adding new Student in Database....")

n1 = Student("prakash", 99)
print(n1.name, n1.marks)


# print(n1)  # It Prints: <__main__.Student object at 0x000001C27C738EC0>
# print(n1.name)  # It Prints: surya




# class Car:
#     color = "Black"
#     brand = 'BMW'

# car1 = Car()
# print(car1.color) # It Print: Black
# print(car1.brand) # It Print: BMW



