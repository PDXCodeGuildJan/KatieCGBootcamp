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
    my_string = "backpack"
    
    l = list(my_string)
    
    l[5] = 'dickbutt'
    
    my_string = ''.join(l)
    
    print(my_string)


# Find a String
def find_a_string():

    s = input("Type in one word, no spaces: ")
    ss = input("Type in the letter you'd like to find: ")
    for i in range(0, len(s)):
        print(s[i])







find_a_string()
