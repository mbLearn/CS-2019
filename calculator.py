# Python Program to Create a Class which Performs Basic Calculator Operations.

"""
Problem Solution
1. Create a class and using a constructor to initialize values of that class.
2. Create methods for adding, substracting, multiplying and dividing two numbers and returning the respective results.
3. Take the two numbers as inputs and create an object for the class passing the two numbers as parameters to the class.
4. Using the object, call the respective function depending on the choice taken from the user.
5. Print the final result.
6. Exit
"""

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

cal = Calc(a, b)

choice = 1

while choice != 0:
    print("To Exit enter 0")
    print("To Add enter 1")
    print("To Subtract enter 2")
    print("To Multiply enter 3")
    print("To Divide enter 4")

    choice = int(input("Enter your choice of operation: "))

    if choice == 1:
        print("\n Result: {} \n" .format(cal.add()))
    elif choice == 2:
        print("\n Result: {} \n" .format(cal.subtract()))
    elif choice == 3:
        print("\n Result: {} \n" .format(cal.multiply()))
    elif choice == 4:
        print("\n Result: {} \n" .format(cal.divide()))
    elif choice == 0:
        print("\n Exiting The Program \n")
    else:
        print("\n Input is Invalid \n")


print()
