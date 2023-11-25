# List is a class, L is object
# Class has rules and functions like L.append
# Cars is a class, Tata Motors is an object....object follows rules of class
#Class has attributes/properties, functions/behaviour
# All data types are class
# Each variable of datatype are object
#object is an instance of class
# Syntax to create an object
# obj name = classname()
s = str()
l = list()
# Pascal Case
# HelloWorld, MyATM, HiFrom

class ATM:

    # constructor # special function -> superpower
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""Hi How can I Help you?
        1. Press 1 to create pin:
        2. Press 2 to change pin:
        3. Press 3 to check balance:
        4. Press 4 to withdraw:
        5. Press anything else to exit: """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter your PIN: ")
        self.pin = user_pin

        user_balance = int(input("Enter Balance: "))
        self.balance = user_balance

        print("PIN Created Sucessfully")
        self.menu()

    def change_pin(self):
        old_pin = input('Enter Old PIN: ')

        if old_pin == self.pin:
        # Let him change the pin

            new_pin = input("Enter New Pin: ")
            self.pin = new_pin
            print("Pin Changed Successfully")

        else:
            print("Wrong Old PIN")
        self.menu()

    def check_balance(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Wrong PIN")
        self.menu()

    def withdraw(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            amt = int(input("Enter the amount"))
            if amt <= self.balance:
                self.balance = self.balance - amt
                print(f"Withdrawl Successful, balance is {self.balance}")
            else:
                print("Not enough money in account")
        else:
            print("PIN is incorrect")
        self.menu()

obj = ATM()
