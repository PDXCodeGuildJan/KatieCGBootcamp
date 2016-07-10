# mixed quotation marks
def mixed_quotes():
    print('Sarah said, "hello, how are you?" and walked off.')


# Add & Remove from lists
def add_rem_list():
    # append to a list
    my_list = ["cup", "backpack", "keys", "charger"]
    print(my_list)
    my_list.append("backpack")
    print(my_list)

    # remove from a list

    my_list.remove("backpack")
    print(my_list)


# Indexing a list
def index_list():

    my_list = ["cup", "backpack", "keys", "charger"]
    print(my_list[0])
    print(my_list[0:3])
    print(my_list)


# Simple Dictionary Demo
def dictionary_play():

    my_dict = {"name": "Katie", "eyes": "Blue"}
    print(my_dict)

    # Add to a Dictionary

    my_dict["Hair"] = "blonde"
    print(my_dict)

    # Look up a value using a key
    print(my_dict["name"])

    del my_dict["name"]
    print(my_dict)


# Basic While Loop
def while_loop_practice():

    temperature = 120
    while temperature > 100:
        print("Your tea is still too hot! it is " + str(temperature) + " degrees!")
        temperature -= 1

    print("You are free to drink your tea!")


# If/Elif/Else Demo
def if_elif_else():

    color = input("What is your favorite color: Red, Blue or Green? ")

    if color == "Red":
        print("Red is an awesome color! You have great taste!")
    elif color == "Blue":
        print("Blue is a wonderful color! Good choice!")
    elif color == "Green":
        print("Who doesn't love green?! Good choice!")
    else:
        print("I didn't say " + color + " was a choice! Try again!")


# Basic For Loop
def for_loop_practice():

    tea = ["Green", "Black", "Herbal", "Chai"]

    for x in tea:
        print("Wow, " + x + " is a great kind of tea!")


# Class Example
class Customer():

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and balance
        is *balance*"""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            print("You cannot withdraw that amount")
        self.balance -= amount
        return self.balance

    def deposit(self, amount):

        self.balance += amount
        return self.balance


def built_in_functions():
    # .upper with strings
    string = "i will print in all uppercase!"
    print(string.upper())
    # .lower with strings
    string = "I WILL PRINT IN ALL LOWERCASE!"
    print(string.lower())

    # .upper/lower demo'd with an if statement
    color = input("What is your favorite color: Red, Blue or Green? ")
        # .upper to convert all characters to uppercase
    if color.upper() == "RED":
        print("Red is an awesome color! You have great taste!")
    elif color.upper() == "BLUE":
        print("Blue is a wonderful color! Good choice!")
        # .lower to convert all characters to lowercase
    elif color.lower() == "green":
        print("Who doesn't love green?! Good choice!")
    else:
        print("I didn't say " + color + " was a choice! Try again!")


def tiger_names():
    tigers = ["Bob", "Sasha", "Boris", "Melanie", "Cupcake"]

    for bob in tigers:     
        print(bob + " is a big cat.")



class Customer():
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            print('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance




