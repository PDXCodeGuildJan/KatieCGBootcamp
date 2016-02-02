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
	

class Angry_Dice:
	"""While Die tracks the dice, Angry_Dice teaches the computer 
		how to play the game."""

	def __init__(self):
		# Creates the first die (die_1) by using the Die class
		self.die_1 = Die()
		# Creates the second die (die_2) by using the Die class
		self.die_2 = Die()
		self.current_round = 1
		self.round_goals = {1:[1,2], 2:[3,4], 3:[5,6]}
		self.winner = False

		

	def start(self):
		"""Greets the user, explains the rules, and starts the game"""

		# print("Let's greet the user!")
		# print("This is fantastic.")
		# print("yayness.")
		# print("I hate this.")
		# input("Press 'S' to start loser.> ")
		# self.check_stage()
		# self.evaluate_dice()

		# while winner = False:
		# 	self.turn()
		# else: 



	def turn(self):
		"""Makes a turn method that asks to hold dies"""
		turn_input = input("What die(s) would you like to hold?> ")
		die_hold(turn_input)




	def evaluate_dice(self):
		"""Evaluates which outcome the roll matches. 
			If the two dice are both angry, start the game over.
			If the two dice both match the round goals, move onto the next round.
			If no double angry or win, roll die/dice again."""
		# Make a while loop that loops through each roll possibility
		#	as long as the roll does not equal two angry faces
		
		# If there are two angry dice
		if self.die_1.value  == 3 and self.die_2.value == 3:
			# Tell the user the dice are angry
			print("Your dice are angry!!! Start over!")
			# Reset the game
			self.current_round = 1

		# If 
		else:
			self.check_stage()

				# Move on to the next round or win
			elif:
				# Move on to ask what die/dice to hold
		pass


	def die_hold(self, turn_input):
		"""A method to hold a die that asks whether or not
		the hold is valid or invalid depending on which
		stage in the game you are on.
		If invalid, tell the user it is invalid and call the roll function
		to roll the die for them again.
		If it is valid, hold the die and roll again."""
		
		# If die_1 in turn_input, check valid
		if die_1 in turn_input:
			if die_1.value == 6 and round_goals == 2:
				# INVALID YOU ARE A BOOB
				print("Invalid. You are a boob. I will roll for you.")
				roll()

			else:
				die_1.is_holding = True

		elif die_2 in turn_input:
			if die_2.value == 6 and round_goals == 2:
				# INVALID YOU ARE A FECKER NOOB FACE
				print("Invalid. You are a noob-faced loser. I will roll for you.")
				roll()
			else:
				die_2.is_holding = True
		else:
			print("That is not valid... that is not... Meh. You suck.")
			roll()


	def check_stage(self):
		
		# Checks to see if the die held or the dice held/rolled are the two 
		#	values needed to proceed to the next round.
		if self.die_1.value in self.round_goals[self.current_round] and self.die_2.value in self.round_goals[self.current_round]:
			 if self.die_1.value != self.die_2.value:
			 	print("You've gone up a level!")
			 	self.current_round += 1

		# If so, stage += 1
		# If not, stage stays the same.
		# If stage completed is stage 2(final stage), proceed to winner winner chicken dinner.

	def winner(self):
		"""Evaluates whether the two valid held dice go on to
		the next round or win the game overall by tracking where
		the player is in the game, round-wise."""
		
		pass

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
		# Two Options:
		# Roll both die each time, no matter if it's being held
		# However, if a die is being held, only display the value it had when it was held

		# or

		# Roll both die until a valid hold has been placed on a die
		# When a die has been held, continue to display it,
		# 	stop rolling it; only roll the other die


		self.value = randint(1, 6)


	def __str__(self):
		"""Print out the rolled and held dice, formatted nicely."""
		return Die.possible_values[self.value]



def test_roll():
	die_1 = Die()
	print(die_1)
	die_1.value = 3
	print(die_1)
	for x in range(2):
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

	