

#Have the user enter the console room, greet them, and let them choose between a few preset directions to go in
#(library[left], swimming pool[forward], or Amy's room[right])
def main():
	print("""You're walking down a busy street when a bright blue old fasioned Police Box catches your eye. 
	After a brief deliberation, you decide to open its doors and walk inside. You are greeted by a voice on what 
	you can only guess is some sort of intercom- but that isn't what surprises you. The inside is massive- much
	larger than what the outside suggested. In fact, it looked to you like the Police Box could go on and on forever;
	with rooms upon rooms upon rooms that you just wanted to explore. Enter 'quit' to exit the program at any time. """)

	entry = ""

	if entry == "quit":
		print("Goodbye!")
		quit()

	console_room()

def console_room():

	print("""The voice spoke. 
	Hello and welcome to the Tardis! That's Time and Relative Dimension in Space, to you! 
	The Doctor is out but I will be your virtual host. You have the freedom
	to go wherever you'd like. There are many rooms to explore. Choose a direction to go and let's get started!
	You have the ability to go left, forward, or right.""")

	direction = ""
	while direction != "quit":

		if direction == "left":
			library()
		elif direction == "forward":
			swimming_pool()
		elif direction == "right":
			ponds_room()
		else: 
			print("I do not understand.")






#This will be the library- maybe introduce the silence??? You can travel to the storage room and swimming pool 
#from the library
 def library():
 	print("""You enter the single most expansive room you've ever seen. Miraculously, no dust seems to have settled anywhere. It's definitely
 		one of the more looked after and popular rooms in the entire place. Ornate wooden bookshelves line the entire perimeter of the room. 
 		Books, old and new, fill the shelves. Near you, very ancient looking scrolls lay atop a large desk. The desk is one of many that
 		take up much of the empty space in the room. There are soft chairs with tables and desk lamps set next to them, couches with 
 		colorful pillows, and piles and piles of books sit on most of the available flat surfaces- including the floor.""")

# 	direction = ""
# 	while direction != "quit":
# 		if direction == up:
# 			storage_room()
# 		elif direction == down:
# 			swimming_pool()
# 		else:
# 			print("I do not understand.")



#This will be the storage room. Describe a few recognizable items- Like Tom Baker's scarf, old sonics, red and blue
#bowties, etc. You will be able to access the library and the circular room from here.
def storage_room():
	print("""You enter a room that is very obviously a storage room. There are shelves everywhere with various items haphazardly
		shoved on them and in every nook and cranny you can see. An colorful over-long scarf hangs from one of the shelves while
		another houses miniature versions of the Tardis. You look around for awhile, but realizing you could spend an 
		entire day in that one room, you decide to move on.""")

	direction = ""
	while direction != "quit":
		direction = input("Would you like to go down or right?")
		if direction == "down":
			library()
		elif direction == "right":
			circular_room()
		else:
			print("I do not understand.")
			storage_room()



#This will be an old, abandoned circular room. Spiders, broken furniture, old writings, chipped china, and a single
#dried rose on a circular table in the center of the room. You will be able to access the storage room and the swimming
#pool from here
def circular_room():
	print("""You enter a perfectly circular room. Giant broken stained glass windows cover most of the stone
		walls while broken chairs, cobwebs, and chipped china litter the floor. There is a small circular table
		in the very center of the room with a single dried rose laid on top of it. You don't understand why, but 
		you're saddened by it- as if it were a reminder of a person or event wanted to be forgotten but always
		cherished. Compelled to move on, you do.""")

	direction = ""
	while direction != "quit":
		direction = input("Would you like to go left or down?")
		if direction == "left":
			storage_room()
		elif direction == "down":
			swimming_pool()
		else: 
			print("I do not understand.")
			circular_room()



#Giant swimming pool. Obviously one of the most popular rooms in the entire tardis. You will be able to access the 
#circular room and the Tardis Console from here
def swimming_pool():
	print("""You enter a room with not much else in it but a giant swimming pool. The edges nearly touch the walls not leaving 
	much room to walk around it. The light reflecting off the pool water dances on the walls and ceiling of the room. You take off your 
	shoes and dip your toes into the pool. You have a feeling that time doesn't matter much here.""")

	direction = ""
	while direction != "quit":
		direction = input("Would you like to go up, left, or down?")
		if direction == "up":
			circular_room()
		elif direction == "left":
			library()
		elif direction == "down":
			console_room()
		else:
			print("I do not understand.")
			swimming_pool()

#Ponds' room. Bunk bed, Amy's childhood drawings of The Doctor... No places to move from here (yet) except for the Console
#room.
def ponds_room():
	print("""You enter a small, cozy bedroom. The walls are covered in childish drawings of a man with crazy hair wearing a blue torn up 
		dress shirt and brown dress pants. It seems to be the character of choice for whomever resides here. There's a good-sized 
		bunkbed pushed into one corner, an over-stuffed chair in another, and curiously, a very authentic looking centurian outfit 
		laying in another.""")

	direction = ""
	while direction != "quit":
		direction =input("You may only go left.")
		if direction == "left":
			console_room()
		else:
			print("I do not understand.")
			ponds_room()

main()

