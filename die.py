from random import randint

def die():
	roll = randint (1, 6)
	print (roll)



def custom_die(low, high):
	roll = randint(low, high)
	if roll == high:
		print(roll, "Critical hit!")
	elif roll == low:
		print(roll, "Critical fail!")
	else:
		print(roll)



def main():
		print ("Welcome to the best die roller in all of the galaxy! Enter a 'q' to exit. ")
		
		entry = ""
		#wrap the core logic of the function in a while loop, 
		#so that it keeps asking to roll until we exit!
		while entry != "q":
			# ask the user how many dice to roll
			entry = input("How many die rolls would you like to roll? ")
			if entry == "q":
				exit()

			total_rolls = int(entry)

			#find out how big the die is
			entry = input("How many sides on the die?")
			if entry == "q":
				exit()

			max_num = int(entry)

			# roll that many dice
			for amount in range (0, total_rolls):
				custom_die(1, max_num)

main()










