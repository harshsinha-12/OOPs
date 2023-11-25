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
    # constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0