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
		# Roll dice to start game off
		game.die_1.roll()
		game.die_2.roll()
		# While the current round of the current game is less than 4:
		while game.current_round < 4:
			# Print out the current round of current game
			print(game.current_round)
			# Print out current die 1
			print(game.die_1)
			# Print out current die 2
			print(game.die_2)
			# Call turn method 
			game.turn()

			game.check_stage()

		# We can later implement a method or function that 
		#	can exit the game no matter when the user inputs an "e"
	elif lets_start.upper() == "E":
		exit()
	

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

		


	def turn(self):
		"""Makes a turn method that asks to hold dies"""
		# Asks the user which die/dice they'd like to hold
		turn_input = input("Would you like to hold die A or B or roll?> ")
		# Call the die_hold method while passing the user input held in the
		#	turn_input variable
		if turn_input.lower() == 'a':
			self.die_hold(turn_input)
		elif turn_input.lower() == 'b':
			self.die_hold(turn_input)

		if self.die_1.is_holding == False:
			self.die_1.roll()

		if self.die_2.is_holding == False:
			self.die_2.roll()


	def die_hold(self, turn_input):
		"""A method to hold a die that asks whether or not
		the hold is valid or invalid depending on which
		stage in the game you are on.
		If invalid, tell the user it is invalid and call the roll function
		to roll the die for them again.
		If it is valid, hold the die and roll again."""
		
		# If die_1 in turn_input, check valid
		if turn_input.lower() == 'a':
			if self.current_round == 1 and (self.die_1.value == 1 or self.die_1.value == 2):
				self.die_1.is_holding = True
			elif self.current_round == 2 and (self.die_1.value == 3 or self.die_1.value == 4):
				self.die_1.is_holding = True
			elif self.current_round == 3 and (self.die_1.value == 5 or self.die_1.value == 6):
				self.die_1.is_holding = True
			else:
				print("You cannot hold a {}. I will roll for you.".format(self.die_1.value))

		elif turn_input.lower() == 'b':
			if self.current_round == 1 and (self.die_2.value == 1 or self.die_2.value == 2):
				self.die_2.is_holding = True
			elif self.current_round == 2 and (self.die_2.value == 3 or self.die_2.value == 4):
				self.die_2.is_holding = True
			elif self.current_round == 3 and (self.die_2.value == 5 or self.die_2.value == 6):
				self.die_2.is_holding = True
			else:
				print("You cannot hold a {}. I will roll for you.".format(self.die_2.value))



	def check_stage(self):
		"""Checks to see if the die/dice rolled change the round to either 
			go up a stage, or go back to stage one.""" 
		# If the value of die_1 is a goal of the current round, and die_2 is a goal of the current round:
		# if self.die_1.value in self.round_goals[self.current_round] and self.die_2.value in self.round_goals[self.current_round]:
		# 	# As long as they're not the same number...
		# 	if self.die_1.value != self.die_2.value:
		# 		# If so, stage += 1
		# 		print("You've gone up a level!")
		# 		self.current_round += 1
		# 		self.die_1.is_holding = False
		# 		self.die_2.is_holding = False

		if self.current_round == 1:
			if (self.die_1.value == 1 or self.die_1.value == 2) and (self.die_2.value == 1 or self.die_2.value == 2) and (self.die_1.value != self.die_2.value):
				print("You've gone up a level!")
				self.current_round = 2
				self.die_1.is_holding = False
				self.die_2.is_holding = False

		elif self.current_round == 2:
			if (self.die_1.value == 3 or self.die_1.value == 4) and (self.die_2.value == 3 or self.die_2.value == 4) and (self.die_1.value != self.die_2.value):
				print("You've gone up a level!")
				self.current_round = 3
				self.die_1.is_holding = False
				self.die_2.is_holding = False

		elif self.current_round == 3:
			if (self.die_1.value == 5 or self.die_1.value == 6) and (self.die_2.value == 5 or self.die_2.value == 6) and (self.die_1.value != self.die_2.value):
				print(game.die_1)
				print(game.die_2)
				self.winner()
				

		elif self.die_1.value == 3 and self.die_2.value == 3:
			print("Two angry!!!! Back to round one!!!")
			self.current_round = 1
			self.die_1.is_holding = False
			self.die_2.is_holding = False



		# If not, stage stays the same.
		# else:
			#self.die_hold()
			# PHASE OUT THESE MOFOS
			#self.turn()
			# Don't level up
			### Roll? ###

	def winner(self):
		"""Winner method to tell the user they've won!"""
		
		print("You've won! Congratulations, the dice are happy!")
		exit()

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
		return self.value


	def __str__(self):
		"""Print out the rolled and held dice, formatted nicely."""
		return Die.possible_values[self.value]

#### TESTS ####
# def test_roll():
# 	die_1 = Die()
# 	print(die_1)
# 	die_1.value = 3
# 	print(die_1)
# 	for x in range(2):
# 		# PHASE OUT THESE MOFOS
# 		die_1.roll()
# 		print(die_1)

# def test_check_stage():
# 	game = Angry_Dice()
# 	game.die_1.value = 1
# 	game.die_2.value = 2
# 	print("Current stage before check: ", game.current_round)
# 	game.check_stage()
# 	print("Current stage after check: ", game.current_round)

game = Angry_Dice()
if __name__ == '__main__':
	main()