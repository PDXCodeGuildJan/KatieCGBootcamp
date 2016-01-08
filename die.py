from random import randint

def die():
	roll = randint (1, 6)
	print (roll)



def custom_die(low, high):
	roll = randint(low, high)
	print (roll)



def main():
	# ask the user how many dice to roll
	total_rolls = input("How many dice rolls would you like to roll? ")
	total_rolls = int(total_rolls)
	#find out how big the die is
	max_num = int(input("How many sides on the dice?"))
	# roll that many dice
	for amount in range (0, total_rolls):
		custom_die(1, max_num)

main()

