# sWAP cASE
def in_one():
    in_one = input("Type a phrase to be replaced: ")

    print(("This is your original phrase: ") + in_one)
    new_phrase = "This is your phrase swapped: " + in_one.swapcase()

    print(new_phrase)


# String Split and Join
def string_split():

    orig_string = input("Type a phrase of two or more words: ")

    split_string = orig_string.split(" ")

    print(split_string)

    join_string = "-".join(split_string)

    print(join_string)


# Mutations
def mutations():

    ex_string = "example"

    print(ex_string[5])

mutations()
