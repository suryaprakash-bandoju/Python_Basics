# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("surya")
# print(s1.name)
# del s1.name # Delete the name
# print(s1.name) # Getting on error




class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass
        
        
acc1 = Account('123123', 'asfdsa')

print(acc1.acc_pass)
print(acc1.acc_no)