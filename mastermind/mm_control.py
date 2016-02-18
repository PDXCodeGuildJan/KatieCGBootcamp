from mm_view import MasterView 
from mm_model import MasterModel, Guess, ColorPeg, HintPeg
import random
import re


def main():
	

	this = MasterMind()
	this.color_picker()
	
	this.guess()


	#this.view.show_start()

class MasterMind:
	def __init__(self):
		self.model = MasterModel()
		self.view = MasterView()


	def start_game(self, show_start, show_rules):
		"""This starts the game. Pings show-start, show_rules from mm_view and introduces rules to player."""

		pass

	def color_picker(self):
		"""Randomly selects four colors color list"""

		num_to_select = 4
		peg_color_list = [] #creates the list to store the peg object

		#write a for loop to set a loop to select 4 colors from SOLUTION in mm_model
		for i in range(num_to_select): #use i just to run the loop, variable is not used elsewhere 
			# print(i)
			color = random.choice(MasterModel.COLORS)
			# print(color)
			#associate color with peg objects
			peg = ColorPeg(color)

			#append the peg_color list to make a list of peg objects 
			peg_color_list.append(peg)
			# print (peg_color_list)
		
		#create object for solution so it can be stored in model.py
		solution = Guess(peg_color_list)

		#put solution into the self.guesses in the model
		self.model.guesses["solution"] = solution


			#Testing Stuff:
		for peg in peg_color_list:
			print(peg.peg_color)

		print(self.model.guesses["solution"])
		

	
	def guess(self):
		""" is the logic that gets user to create a guess, then assigns that guess to peg objects,
		so that guess can be evaluated against color_picker (def eval guess) and called again as part of def big display."""
		
		peg_guess_color_list = []
		guess_input = self.view.input_guess()

		# Convert guess_input into a list- each color being a string
		guess_color_list = re.split(",", guess_input)
		

		for each_color in guess_color_list:

			### TESTS ###
			print ("This is each color: ", each_color)
			# print ("print guess input again: ", guess_input)

			#associate each string with a peg object
			peg_guess = ColorPeg(each_color)
			print("prints each peg color for guess: ", peg_guess)
			
			# make a list of the objects
			# Append the peg_guess color list to make a list of peg guess objects
			
			peg_guess_color_list.append(peg_guess)

			# Plug our peg objects into our guess object
			guess = Guess(peg_guess_color_list)

			# Store guess object in our MasterModel
			self.model.guesses["Guess 1"] = guess


		### TESTS ###
		print("Prints the list of color guesses: ", peg_guess_color_list)
		for peg_guess in peg_guess_color_list:
			print("Prints the list of guess pegs: ", peg_guess.peg_color)

		print("Prints out the first list of guesses. Key = Guess 1", self.model.guesses["Guess 1"])


	def eval_guess(self, color_picker, imput_guess):
		"""evaluates input received from player against color_picker to determine win / true vs no win / false."""
		pass

	def eval_status(self, input_guess, status):
		"""Evaluates where player is in the game, the "round", if 10 or more rounds = player looses; if 9 or less, player guess again """


		pass
	
	def guess_response(self, Guess):
		"""response to user guess after check status and status is less than or equal to 9, produces 'big-display' to update
		player on their status, pins and pegs, etc. """


		pass
	

	def exit(self, show_exit):
		"An exit function that will be avialable to players throughout all parts of the game."
		pass

if __name__ == '__main__':
	main()




