import mm_view
import mm_model
import random

class MasterMind:
	def __init__(self):
		pass

	def color_picker(self):
		"""Randomly selects four colors from color list"""

		num_to_select = 4

		#write a for loop to set a loop to select 4 colors from SOLUTION in mm_model
		for i in range(num_to_select): #use X since it is needed to get the loop to run
			color = random.choice(mm_model.MasterModel.COLORS)

			#make the color a peg
			# PEGCOLOR = [color.append]

			#append the peg to make a list of pegs of no more than 4
		

			print(i)
			print(color)




		
		# self.random_solution = random.sample(self.solution, num_to_select)
		# return self.random_solution

		
	def start_game(self, show_start):
		pass
	
	def eval_status(self, input_guess, status):
		pass
	
	def guess_response(self, Guess):
		pass
	
	def eval_response(self, solution, imput_guess):
		pass

	def exit(self, show_exit):
		pass

this = MasterMind()
this.color_picker()




