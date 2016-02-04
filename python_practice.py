from random import randint


def main():
	given_values = [1,2,3,4,5,6] 
	d6 = Die(given_values)
	d6.roll()
	print(d6)

class Die:
	""" Creates a die class that allows users to pass a list of values
		that serve as the die's sides."""

	def __init__(self, given_values):
		self.current_index = 0
		self.possible_values = given_values

	def roll(self):
		self.current_index = randint(0, len(self.possible_values) -1)
		#print(self)

	def __str__(self):
		return str(self.possible_values[self.current_index])




if __name__ == '__main__':
	main()