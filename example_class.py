# Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.
# Encapsulation: Wrapping data and function into a single unit (object).


# class Car:
#     def __init__(self):
#         self.acc    = False
#         self.brk    = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc    = True
#         print("Car is Started")

# car1 = Car()
# car1.start()


class Account:
    def __init__(self, bal, acc):
        self.balance    = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs {amount} was debited")
        print(f"Total balance: {self.get_balance()}")

    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} was credited")
        print(f"Total balance: {self.get_balance()}")

    def get_balance(self):
            return self.balance

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(6000)
