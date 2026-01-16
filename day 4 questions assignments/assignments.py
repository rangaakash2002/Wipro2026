#Define the student class
# class Student:
#     def __init__(self,name,roll_no):
#         self.name=name
#         self.roll_no=roll_no
#     def display_details(self):
#         print(f"name:{self.name}")
#         print(f"Roll no:{self.roll_no}")
#         print("-"*30)
# student1= Student("Akash",23)
# Student2= Student("sai",34)
# student1.display_details()
# student2.display_details()


#2
class BankAccount:

    # Parameterized constructor
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Account created")

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        else:
            self.balance += amount
            print("Amount deposited:", amount)

    # Withdraw method with checks
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)

    # Destructor
    def __del__(self):
        print("Account deleted")


# Creating object
acc = BankAccount("866985868", 5000)

# Taking input from user
deposit_amt = int(input("Enter deposit amount: "))
acc.deposit(deposit_amt)

withdraw_amt = int(input("Enter withdraw amount: "))
acc.withdraw(withdraw_amt)
