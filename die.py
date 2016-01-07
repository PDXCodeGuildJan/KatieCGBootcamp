# Create a die function that returns a random number as if the user rolled a die

from random import randint

# def die():
# 	roll = randint (1, 6)
# 	print (roll)

# die()

def custom_die(low, high):
	roll = randint(low, high)
	print (roll)


custom_die(90, 800)