class MasterModel:
	"""a class for the creation and storing guess, color, and status objects"""
	# Const for selection of color peg solution and guesses.

	COLORS = ["Blu", "Blk", "Yel", "Red", "Grn", "Wte"]

	def __init__(self):
		
		self.guesses = {} # To be a dictionary of peg objects for guesses and the solution. Key: int(1-10) 
							# Value: Guess object 
		self.status = 1



class Guess:
	"""for creation and storage of user guess and response objects"""
	def __init__(self, peg_list):
		self.hint_response = []
		self.pegs = peg_list 
	
	def __str__(self):
		new_string = ""
		for x in self.pegs:	
			new_string += str(x)
		return new_string

class ColorPegGuess:
	"""This is a creation of storage for current and past guesses"""
	pass

class ColorPeg:
	"""for creation and storage of colorpeg objects for color picker"""
	
	def __init__(self, color):
		self.peg_color = color
	
	def __str__(self):
		return self.peg_color

class HintPeg:
	"""for creation and storage of hint peg responses"""

	PEGS = ["Blk", "Wht"]

	def __init__():
		peg_type = "" #CONST

	pass


