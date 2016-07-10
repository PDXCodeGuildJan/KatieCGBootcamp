
def strings():
    """Things you can do with strings"""

    x = "the hair hobbit hobbled hardly"

    "cat".capitalize()  # .capitalize

    # .split
    x.split()

    # .lower
    x.lower()

    #.format
    'the {} wizard'.format('cute')

    # .upper
    x.upper()

    # .isdigit
    'cat'.isdigit()
    '34'.isdigit()

    # .join
    s = '+'
    s.join(x)

    print(s.join(x.split()))

    # .isupper
    x.isupper()

    # .strip
    w = "     dfdfd     "
    print(w.strip())


def integers():
    """Things you can do with Integers"""

    # Will return the remainder if 10 is divided by 3
    modo = 10 % 3
    print(modo)
    # Will return 1

    # Integer division
    i_d = 11 // 5
    print(i_d)
    # Will return 2

    # Normal Integer division
    nid = 11 / 5
    print(nid)
    # Will return 2.2


def booleans():
    """Fun with booleans. True or False!"""

    true = 1 == 1  # return true
    print(true)
    false = 3 == 1  # return false
    print(false)

    # If ANY are true, return true
    any([True, False, False])

    # If all contain False
    any([False, False, False])

    # will return bool
    type(True)


def list_practice():
    """ Practice lists """
    my_list = [4, 5, 6, 7, 8]
    print(my_list)

    # Add two lists
    print(my_list + my_list)

    # Multipy lists
    print(my_list * 3)

    # Add an item to a list
    my_list.append(9)
    print(my_list)

    # Print out a single value
    print(my_list[3])

    # Print out reverse- will print out last item
    print(my_list[-1])

    # Tell me the index of item 7 in list
    print(my_list.index(7))


def sets():
    li = list(range(10000))

    si = set(li)

    value = li[-1]

    print(value in li)
    print(value in si)


def dicts():
    dictionary = {"cat": 5}
    print(dictionary['cat'])

def tuples():
    # Two methods: count & index

    # Empty tuple
    x = tuple()
    print(x)

    # Create a tuple
    x = (5, 53, 6, 75)
    print(x)

    # Print out third index in tuple
    print(x[3])


def if_statement_practice():

    if 1 == 1:
        print("cat")

    x = "I am a cat!"

    # If the first character in x is "I"
    if x.upper()[0] == "I":
        print("yes")
    else:
        print("no")

    # Is first character a alphabetic character
    if x[0].isalpha():
        print("You know your ABC's!")
    else:
        print("You do not know your ABC's...")

    if 0:
        print("zero is true")
    else:
        print("zero is false")


def for_loops():
    x = "I am a cat!"
    # For loop will print out each character in x
    # Takes whitespace into account
    for element in x:
        print(element)
    # Ignores whitespace
    for element in x.split():
        print(element)


def while_loops():
    i = 0
    while i < 10:
        print(i)
        i += 1

    x = 0
    while x > 10:
        print(x)
        x -= 1

    while False:
        print("I will never print")

    while True:
        print("This will print...FOREVER!")

while_loops()
