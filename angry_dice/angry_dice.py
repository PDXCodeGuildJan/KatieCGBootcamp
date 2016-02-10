"""Angry Dice is a game to be played by yourself or with a partner. 
	Simply roll numbers 1-6 sequentially to win the game. There are three rounds. 
	Round 1 Goal: roll both a 1 and a 2 to move onto round 2.
		Roll two dice until you roll a 1, a 2, or both a 1 and a 2.
		Hold one of the dies if you roll a 1 or a 2.
		Roll the remaining die until you roll a the remaining number you need.
		When you have both values you need, move on to the next round.
		If you roll two angry dice, start over.
	Round 2 Goal: Roll both a 3 and an angry die to move onto the final round.
		Very similar to round 1, roll and hold until you have an angry die and a 4.
		When you have both values you need, move on to the next round.
		If you roll two angry dice, start over.
	Round 3 Goal: Roll both a 5 and 6 to win!
		You may hold a 5, but you may not hold a six. You must either roll a 5 and a
		6 simultaniously, or hold a 5 before holding a six.
		When you have both values you need, your game ends.
		If you roll two angry dice, start over.
	The first player to get through all three rounds wins!
	"""

__author__ = "Katie Dover"

from random import randint

def main():
	"""Use this for testing the code."""
	print("""
	      ____  ____    ____  ____   __ __      ___    ____    __    ___ 
|\\```````\\   /    ||    \\  /    ||    \\ |  |  |    |   \\  |    |  /  ]  /  _]
| |```````| |  o  ||  _  ||   __||  D  )|  |  |    |    \  |  |  /  /  /  [_ 
| | \\   / | |     ||  |  ||  |  ||    / |     |    |  D  | |  | /  /  |    _]
| | ^   ^ | |  _  ||  |  ||  |_ ||    \\ |___, |    |     | |  |/   \\_ |   [_
 \\| ----- | |  |  ||  |  ||     ||  .  \\|     |    |     | |  |\\     ||     |
  ````````` |__|__||__|__||___,_||__|\\_||____/     |_____||____|\\____||_____|
 """)
	

class Angry_Dice:
	"""While Die tracks the dice, Angry_Dice teaches the computer 
		how to play the game."""

	def __init__(self):
		"""Creates two dice to play with. Sets the current round to 1.
		Creates a dictionary that holds the goals for each round."""
		# Creates the first die (die_1) by using the Die class
		self.die_1 = Die()
		# Creates the second die (die_2) by using the Die class
		self.die_2 = Die()
		# Sets the current round at 1 to start out
		self.current_round = 1
		# Creates the round goals dict with goals for each round
		self.round_goals = {1:[1,2], 2:[3,4], 3:[5,6]}
		


		# Sets the winner bool to False
		# Is this even necessary?
		# I have it in my start() but still unclear if I need it.
		# Especially because I want to re-write the start().
		self.winner = False

		

	def start(self):
		"""Greets the user, explains the rules, and starts the game"""
		print("""
			  ____  ____    ____  ____   __ __      ___    ____    __    ___ 
|\\```````\\   /    ||    \\  /    ||    \\ |  |  |    |   \\  |    |  /  ]  /  _]
| |```````| |  o  ||  _  ||   __||  D  )|  |  |    |    \  |  |  /  /  /  [_ 
| | \\   / | |     ||  |  ||  |  ||    / |     |    |  D  | |  | /  /  |    _]
| | ^   ^ | |  _  ||  |  ||  |_ ||    \\ |___, |    |     | |  |/   \\_ |   [_
 \\| ----- | |  |  ||  |  ||     ||  .  \\|     |    |     | |  |\\     ||     |
  ````````` |__|__||__|__||___,_||__|\\_||____/     |_____||____|\\____||_____|

			""")
		print("""
\n\n
\t\t\tRules:
\t\t\t______
\tAngry Dice is a game to be played by yourself or with a partner.
\tSimply roll numbers 1-6 sequentially to win the game. There are three rounds. 

\tRound 1 Goal: Roll both a 1 and a 2 to move onto round 2.
	\tRoll two dice until you roll a 1, a 2, or both a 1 and a 2.
	\tHold one of the dies if you roll a 1 or a 2.
	\tRoll the remaining die until you roll a the remaining number you need.
	\tWhen you have both values you need, move on to the next round.
	\tIf you roll two angry dice, start over.
\tRound 2 Goal: Roll both a 3 and an angry die to move onto the final round.
	\tVery similar to round 1, roll and hold until you have an angry die and a 4.
	\tWhen you have both values you need, move on to the next round.
	\tIf you roll two angry dice, start over.
\tRound 3 Goal: Roll both a 5 and 6 to win!
	\tYou may hold a 5, but you may not hold a 6. You must either roll a 5 and a
	\t6 simultaniously, or hold a 5 before holding a 6.
	\tWhen you have both values you need, your game ends.
	\tIf you roll two angry dice, start over.
\tIf you are playing with a partner, the first player to get through 
\tall three rounds wins!""")

		lets_start = input("Press 'S' to start, 'E' to exit. Good luck!> ")

		if lets_start.upper() == "S":
			# We need to make a one off dice roll
			# Then send that one off to evaluate dice
			while current_round < 4:
				# loop through
				# each function
				# to run through each one
				# if I can do that...?

		# We can later implement a method or function that 
		#	can exit the game no matter when the user inputs an "e"
		elif lets_start.upper() == "E":
			exit()




		# Print out two random dice.
		# Print out a prompt with two options:
		# Hold die A and/or B
		# Exit
		# self.check_stage()
		# self.evaluate_dice()

		# while winner = False:
		# 	self.turn()
		# else: 

		pass


	def turn(self):
		"""Makes a turn method that asks to hold dies"""
		# Asks the user which die/dice they'd like to hold
		turn_input = input("What die(s) would you like to hold?> ")
		# Call the die_hold method while passing the user input held in the
		#	turn_input variable
		die_hold(turn_input)




	def evaluate_dice(self):
		"""Evaluates which outcome the roll matches. 
			If the two dice are both angry, start the game over.
			If the two dice both match the round goals, move onto the next round.
			If no double angry or win, roll die/dice again."""
		
		# If there are two angry dice
		if self.die_1.value  == 3 and self.die_2.value == 3:
			# Tell the user the dice are angry
			print("Your dice are angry!!! Start over!")
			# Reset the game
			self.current_round = 1


		# If not two angry dice
		else:
			# Call the check_stage method to check which stage the user is going into
			self.check_stage()
			# If the user is going OUT of the final round, they win!
			if self.current_round == 4:
				# Call the winner method to trigger the winning message!
				# GET RID OF THIS!
				#self.winner()

	def die_hold(self, turn_input):
		"""A method to hold a die that asks whether or not
		the hold is valid or invalid depending on which
		stage in the game you are on.
		If invalid, tell the user it is invalid and call the roll function
		to roll the die for them again.
		If it is valid, hold the die and roll again."""
		
		# If die_1 in turn_input, check valid
		if die_1 in turn_input:
			if die_1.value == 6 and round_goals == 3:
				# INVALID YOU ARE A BOOB
				print("You cannot hold a 6. I will roll for you.")
				# PHASE OUT THESE MOFOS
				#roll()
			elif die_1.value == # Is what's needed for current_round:
				if # Is valid:
					die_1.is_holding = True
					#hold, roll
				else: #not valid
					#don't hold, roll

		elif die_2 in turn_input:
			if die_2.value == 6 and round_goals == 3:
				# INVALID YOU ARE A FECKER NOOB FACE
				print("You cannot hold a 6. I will roll for you.")
				# PHASE OUT THESE MOFOS
				#roll()
			elif die_2.value == # Is what's needed for current round:
				if # Is valid:
					die_2.is_holding = True
		else:
			print("Invalid input. Please enter in a number 1-6.")
			# roll again, but not by calling the roll method
			#roll()


	def check_stage(self):
		"""Checks to see if the die held or the dice held/rolled are the two 
		values needed to proceed to the next round.""" 
		# If the value of die_1 is a goal of the current round, and die_2 is a goal of the current round:
		if self.die_1.value in self.round_goals[self.current_round] and self.die_2.value in self.round_goals[self.current_round]:
			 # As long as they're not the same number...
			 if self.die_1.value != self.die_2.value:
			 	# If so, stage += 1
			 	print("You've gone up a level!")
			 	self.current_round += 1


		# If not, stage stays the same.
		else:
			#self.die_hold()
			# PHASE OUT THESE MOFOS
			#self.turn()
			# Don't level up
			### Roll? ###

	def winner(self):
		"""Winner method to tell the user they've won!"""
		
		print("You've won! Congratulations, the dice are happy!")

class Die:
	"""Tracks the set of dice individually when playing the game."""
	possible_values = {

	1:  
"""
+-------+
|       |
|   o   |	
|       |
+-------+""", 
	2: 
"""
+-------+
| o     |
|       |
|     o |
+-------+""",
	3: 
"""
+-------+
| \   / |
| ^   ^ |
| ----- |
+-------+""",
	4: 
"""
+-------+
| o   o |
|       |
| o   o |
+-------+""",
	5: 
"""
+-------+
| o   o |
|   o   |
| o   o |
+-------+""",
	6: 
"""
+-------+
| o   o |
| o   o |
| o   o |
+-------+
	"""
		}
	
	def __init__(self):
		self.value = 1
		self.is_holding = False


	def roll(self):
		"""Randomly roll the die/dice. Can roll two simultaniously or
			roll one die while holding the other."""

		self.value = randint(1, 6)


	def __str__(self):
		"""Print out the rolled and held dice, formatted nicely."""
		return Die.possible_values[self.value]

#### TESTS ####

def test_roll():
	die_1 = Die()
	print(die_1)
	die_1.value = 3
	print(die_1)
	for x in range(2):
		# PHASE OUT THESE MOFOS
		die_1.roll()
		print(die_1)

def test_check_stage():
	game = Angry_Dice()
	game.die_1.value = 1
	game.die_2.value = 2
	print("Current stage before check: ", game.current_round)
	game.check_stage()
	print("Current stage after check: ", game.current_round)


if __name__ == '__main__':
	main()

	