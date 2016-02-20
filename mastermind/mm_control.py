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

		#put solution into the self.guesses dictionary in the model
		self.model.guesses["solution"] = solution


		#Testing Stuff:
		# for peg in peg_color_list:
		# 	print(peg.peg_color)

		# print(self.model.guesses["solution"])
		

	
	def guess(self):
		""" is the logic that gets user to create a guess, then assigns that guess to peg objects,
		so that guess can be evaluated against color_picker (def eval guess) and called again as part of def big display."""
		
		peg_guess_color_list = []
		guess_input = self.view.input_guess()

		# Convert guess_input into a list- each color being a string
		guess_color_list = re.split(",", guess_input)
		

		for each_color in guess_color_list:

			#associate each string with a peg object
			peg_guess = ColorPeg(each_color)
			
			# Append the peg_guess color list to make a list of peg guess objects
			peg_guess_color_list.append(peg_guess)

			# Plug our peg objects into our guess object
			user_guess = Guess(peg_guess_color_list)

			# Store guess object in our MasterModel
			self.model.guesses["Guess 1"] = user_guess

			# Make a variable that


		# ### TESTS ###
		# print ("This is each color: ", each_color)
		# print ("print guess input again: ", guess_input)
		# print("prints each peg color for guess: ", peg_guess)
		# print("Prints the list of color guesses: ", peg_guess_color_list)
		# for peg_guess in peg_guess_color_list:
		# 	print("Prints the list of guess pegs: ", peg_guess.peg_color)

		# print("Prints out the first list of guesses. Key = Guess 1", self.model.guesses["Guess 1"])


	def win_check(self, color_picker, imput_guess):
		"""evaluates input received from player against color_picker to determine win / true vs no win / false."""

		# retrieve peg_guess_color_list for current round

		# retreive solution list

		# compare values in each index for both lists against eachother

		# if all values in each list match eachother, produce a true value and prompt win

		# if any of the values in each list do not match, produce a false value and promopt check_status method 
		pass

	def check_status(self, win_check, model_status):
		"""checks status or round for player, if round is => 10, prompt loose, if round is <= 9, prompt eval_status"""

		# retreives false value from win_check

		# compare against current status, 

		# if status is >= 10 prompt loose

		# if status is <= 9, prompt eval guess

		pass
	
	def eval_guess(self, Guess):
		"""response to user guess after check status and status is less than or equal to 9, produces 'big-display' to update
		player on their status, pins and pegs, etc. """

		# pulls comparison from win check and assigns peg responses 

		# returns a list to be in hint_response

		# displays as part of big display in view.

		pass
	
	def round_advance(self):
		"""advances round counter by one"""

		# takes current round and advances it by one.
		if self.model.status <= 9:
			
			self.model.status += 1	

	

	def exit(self, show_exit):
		"An exit function that will be avialable to players throughout all parts of the game."
		pass

if __name__ == '__main__':
	main()




