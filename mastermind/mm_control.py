from mm_view import MasterView, 
from mm_model import MasterModel, Guess, ColorPeg, HintPeg
import random


def main():
	pass

class MasterMind:
	def __init__(self):
		pass

	def start_game(self, show_start, show_rules):
		"""This starts the game. Pings show-start, show_rules from mm_view and introduces rules to player."""

		pass

	def color_picker(self):
		"""Randomly selects four colors color list"""

		num_to_select = 4
		peg_color_list = [] #creates the list to store the peg object

		#write a for loop to set a loop to select 4 colors from SOLUTION in mm_model
		for i in range(num_to_select): #use i just to run the loop, variable is not used elsewhere 
			color = random.choice(MasterModel.COLORS)

			#associate color with peg objects
			peg = ColorPeg(color)

			#append the peg_color list to make a list of peg objects 
			peg_color_list.append(peg)

		
		# 	Testing Stuff:
		# 	print(i)
		# 	print(color)
		# print (peg_color_list)
		# for peg in peg_color_list:
		# 	print(peg.peg_color)
		

	
	def Guess(self):
		""" is the logic that gets user to create a guess, then assigns that guess to peg objects,
		so that guess can be evaluated against color_picker (def eval guess) and called again as part of def big display."""
		guess_colors = MasterView.input_guess.guess_input()
		# Convert guess_input into a list- each color being a string

		# Convery new list of strings into a list of peg objects(peg_1, peg_2, peg_3, peg_4)

		# Plug our peg objects into our guess object

		# Store guess object in our MasterModel
		
		pass

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
	# main()

	this = MasterMind()
	this.color_picker()

	# mm_view.MasterView.show_start()



