# mixed quotation marks

# print("Sarah said, "hello, how are you?" and walked off.")

# append to a list

my_list = ["cup", "backpack", "keys", "charger"]
print(my_list)
my_list.append("backpack")
print(my_list)

# remove from a list

my_list.remove("backpack")
print(my_list)

# Indexing a list

print(my_list[0])
print(my_list[0:3])
print(my_list)

# Simple Dictionary Demo

my_dict = {"name": "Katie", "eyes": "Blue"}
print(my_dict)

# Add to a Dictionary

my_dict["Hair"]  = "blonde"
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

if_elif_else()  
