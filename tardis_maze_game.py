

#Have the user enter the console room, greet them, and let them choose between a few preset directions to go in
#(library[left], swimming pool[forward], or Amy's room[right])
def main(direction):
    if direction.lower() == "quit":
        print("Please come back to play again soon! Goodbye!")
        quit()


    console_room()

def console_room():
    print("""
     _____                                                                              
    /__   \ __ _  _ __  _| |(_) ___    /__\__  __ _ __  | |  ___   _ __  ___  _ __ 
     / /\// _` || '__|/ _` || |/ __|  /_\  \ \/ /| '_ \ | | / _ \ | '__|/ _ \| '__|
    / /  | (_| || |  | (_| || |\__ \ //__   >  < | |_) || || (_) || |  |  __/| |   
    \/    \__,_||_|   \__,_||_||___/ \__/  /_/\_\| .__/ |_| \___/ |_|   \___||_|   
                                                 |_|                               


You're walking down a busy street when a bright blue old fasioned Police Box catches your eye. 
After a brief deliberation, you decide to open its doors and walk inside. You are greeted by a voice on what 
you can only guess is some sort of intercom- but that isn't what surprises you. The inside is massive- much
larger than what the outside suggested. In fact, it looked to you like the Police Box could go on and on forever;
with rooms upon rooms upon rooms that you just wanted to explore.
-------
The voice spoke. 
Hello and welcome to the Tardis! That's Time and Relative Dimension in Space, to you! 
The Doctor is out but I will be your virtual host. You have the freedom
to go wherever you'd like. There are many rooms to explore. Choose a direction to go and let's get started!
You have the ability to go left, forward, or right. Enter 'quit' to exit the program at any time.
-----------------------------------
 """)

    
    direction = input ("Would you like to go LEFT, FORWARD, or RIGHT?> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "left":
            print("You head through a long corridor...")
            library()
        elif direction == "forward":
            print("You walk through a hallway completely covered in white tile...")
            swimming_pool()
        elif direction == "right":
            print("You take the door on your right and you are immediately taken through to a parlor much like your Grandmother's...")
            ponds_room()
        else: 
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            console_room()
    
    main(direction)


def console_room_two():
    print("""You find yourself back in the console room. You can either leave the Tardis or continue to explore.
-----------------------------------
""")

    direction = input ("Would you like to go BACK to exit the tardis, or LEFT, FORWARD, or RIGHT?> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "back":
            print("You exit the Tardis. I hope you had fun exploring!")
            exit()
        elif direction == "left":
            print("You head through a long corridor... ")
            library()
        elif direction == "forward":
            print("You walk through a hallway completely covered in white tile... ")
            swimming_pool()
        elif direction == "right":
            print("You take the door on your right and your are immediately taken through to a parlor much like your Grandmother's... ")
            ponds_room()
        else:
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            console_room_two()

    main(direction)


#This will be the library- maybe introduce the silence??? You can travel to the storage room and swimming pool 
#from the library
def library():
    print("""You enter the single most expansive room you've ever seen. Miraculously, no dust seems to have settled anywhere. It's definitely
one of the more looked after and popular rooms in the entire place. Ornate wooden bookshelves line the entire perimeter of the room. 
Books, old and new, fill the shelves. Near you, very ancient looking scrolls lay atop a large desk. The desk is one of many that
take up much of the empty space in the room. There are soft chairs with tables and desk lamps set next to them, couches with 
colorful pillows, and piles and piles of books sit on most of the available flat surfaces- including the floor. "Hearing a loud noise, 
you shake with a start. Not wanting to stick around to find out who or what made the sound, you look towards the only two exits. 
-----------------------------------
""")

    direction = input ("Would you like to go UP or DOWN?> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "up":
            print("You head through a stone archway... ")
            storage_room()
        elif direction == "down":
            print ("You walk through a hallway completely covered in white tile... ")
            swimming_pool()
        else:
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            library()

    main(direction)



#This will be the storage room. Describe a few recognizable items- Like Tom Baker's scarf, old sonics, red and blue
#bowties, etc. You will be able to access the library and the circular room from here.
def storage_room():
    print("""You enter a room that is very obviously a storage room. There are shelves everywhere with various items haphazardly
shoved on them and in every nook and cranny you can see. An colorful over-long scarf hangs from one of the shelves while
another houses miniature versions of the Tardis. You look around for awhile, but realizing you could spend an 
entire day in that one room, you decide to move on. 
-----------------------------------
""")

    direction = input("Would you like to go DOWN or RIGHT?> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "down":
            library()
        elif direction == "right":
            circular_room()
        else:
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            storage_room()

    main(direction)



#This will be an old, abandoned circular room. Spiders, broken furniture, old writings, chipped china, and a single
#dried rose on a circular table in the center of the room. You will be able to access the storage room and the swimming
#pool from here
def circular_room():
    print("""You enter a perfectly circular room. Giant broken stained glass windows cover most of the stone
walls while broken chairs, cobwebs, and chipped china litter the floor. There is a small circular table
in the very center of the room with a single dried rose laid on top of it. You don't understand why, but 
you're saddened by it- as if it were a reminder of a person or event wanted to be forgotten but always
cherished. Compelled to move on, you do.
-----------------------------------
""")

    direction = input("Would you like to go LEFT, RIGHT or DOWN?> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "left":
            storage_room()
        elif direction == "right":
            print("""You go through a large wooden door. The floor vanishes beneath your feet and suddenly... """)
            trap_room()
        elif direction == "down":
            swimming_pool()
        else: 
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            circular_room()

    main(direction)

def trap_room():
    print("""the you are lying on a large net made of very thick rope. You must escape. Going back the way you
came isn't an option, there's no way to get up to thewooden door you came through.
You have a knife in your pocket. There's a window not far from you- you could probably climb
through it. Or you could stay and wait for help.
-----------------------------------
""")

    direction = input("Would you like to use the KNIFE, WINDOW, or HELP?> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "knife":
            knife_scenario()
        elif direction == "window":
            window_scenario()
        elif direction == "help":
            help_scenario()
        else:
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            trap_room()

    main(direction)

def knife_scenario():
    print("""You take out your pocket knife and start sawing at the ropes. They're very thick. Your knife breaks.
Cutting the ropes is no longer an option.
-----------------------------------
""")

    direction = input("Would you like to use the WINDOW, HELP, or EXIT?> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "window":
            window_scenario()
        elif direction == "help":
            help_scenario()
        elif direction == "exit":
            print("""You close your eyes and wish to be home. To your shock, you open your eyes and you're back in your bed.
                perhaps it was all a dream....""")
            quit()
        else: 
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            knife_scenario()

    main(direction)


def window_scenario():
    print("""You carefully climb over the ropes until you're sitting on the ledge of the window. You look down. Blackness.
There's no way to see what's below but you jump anyway. You're floating through nothing for what seems
like an eternity. Suddenly you're surrounded by water... A swimming pool!
-----------------------------------
""")
    
    swimming_pool()


def help_scenario():
    print("""You start calling for help. You don't know how much time has passed, but your voice is growning hoarse and quiet.
The Tardis is so large. There's no way anyone is going to find you here before you starve to death.
-----------------------------------
""")

    direction = input("Would you like to use the WINDOW, KNIFE, or EXIT?> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "window":
            window_scenario()
        elif direction == "knife":
            knife_scenario()
        elif direction == "exit":
            print("""You close your eyes and wish to be home. To your shock, you open your eyes and you're back in your bed.
                perhaps it was all a dream....""")
            quit()
        else: 
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            help_scenario()

    main(direction)



#Giant swimming pool. Obviously one of the most popular rooms in the entire tardis. You will be able to access the 
#circular room and the Tardis Console from here
def swimming_pool():
    print("""You enter a room with not much else in it but a giant swimming pool. The edges nearly touch the walls not leaving 
much room to walk around it. The light reflecting off the pool water dances on the walls and ceiling of the room. You take off your 
shoes and dip your toes into the pool. You have a feeling that time doesn't matter much here.
-----------------------------------
""")

    direction = input("Would you like to go UP, LEFT, or DOWN?> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "up":
            circular_room()
        elif direction == "left":
            library()
        elif direction == "down":
            console_room_two()
        else:
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            swimming_pool()

    main(direction)

#Ponds' room. Bunk bed, Amy's childhood drawings of The Doctor... No places to move from here (yet) except for the Console
#room.
def ponds_room():
    print("""You enter a small, cozy bedroom. The walls are covered in childish drawings of a man with crazy hair wearing a blue torn up 
dress shirt and brown dress pants. It seems to be the character of choice for whomever resides here. There's a good-sized 
bunkbed pushed into one corner, an over-stuffed chair in another, and curiously, a very authentic looking centurian outfit 
laying in another.
-----------------------------------
""")

    direction = input("You may only go LEFT.> ")
    while direction.lower() != "quit":
        direction = direction.lower()
        if direction == "left":
            console_room_two()
        else:
            print("""
                -----------------------------------
                I do not understand.
                -----------------------------------
                """)
            ponds_room()
    
    main(direction)

console_room()
