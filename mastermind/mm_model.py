class MasterModel:
	"""a class for the creation and storing guess, color, and status objects"""
	# Const for selection of color peg solution and guesses.

	COLORS = ["Blu", "Blk", "Yel", "Red", "Grn", "Wte"]

	def __init__(self):
		
		self.guesses = {} # To be a dictionary of guess objects. Key: int(1-10) 
							# Value: Guess object
		self.status = 1

	"""need a place to store solution, could this be in the dictionary
	we are making for storing user guesses?"""

class Guess:
	"""for creation and storage of user guess and response objects"""
	def __init__(self, peg_list):
		#self.hint_response = {[HintPeg]}
		self.pegs = peg_list 
		

class ColorPegGuess:
	"""This is a creation of storage for current and past guesses"""
	pass

class ColorPeg:
	"""for creation and storage of colorpeg objects for color picker"""
	
	def __init__(self, color):
		self.peg_color = color
	

class HintPeg:
	"""for creation and storage of hint peg responses"""

	PEGS = ["Blk", "Wht"]

	def __init__():
		peg_type = "" #CONST

	pass


