class MasterView:

	def big_display(self, show_past_guess, show_status, show_pegs, show_curr_guess):
		"""combines all above infomation into cohsieve display to user."""
		pass

	def show_curr_guess(self):
		"""displays the current guess, is a part of big display"""
		print("Your current guess is: ", current_guess)
		# Have the controller retrieve the current guess from model; insert here! 
		

	def show_past_guess(self, guess_response):
		"""shows players past guesses"""
		print("""Your past guesses are: \n""",
		guesses)
	
	def show_status(self, status):
		""" shows players current status a.k.a. round """
		print("You are currently on round ", check_status)
	
	def show_pegs(self, guess_response):
		"""shows black and white pegs as part of big display"""
		# Display the black/white peg dict
	
	def show_solution(self, solution):
		"""shows colors chosen as part of color_picker to player at end of game, exit, or win. """
		print("The solution was: ", solution)
	
	def show_rules(self):
		"""Shows the user all Mastermind rules at any time during game play."""
		rules_menu_input = input("""
Rules:
\n
Try to figure out the secret code in 10 or fewer guesses.\n
\n
You are the codebreaker, the computer is the code maker. \n
\n
The computer will generate a secret code consisting of 4 color pegs from six color options:\n
 \nRed, Green, Blue, Black, Yellow, and White. \n
\n
You, the code breaker, will use guesses to figure out the secret code.
\n
A guess is made up of 4 colors using  any combination of the six provided colors.  
\n
 After each guess the computer will evaluate the guess against the secret code, if it matches, you win. if not, the computer will provide feedback as follows:\n
\n
A Black Indicator Peg shows if a correct color i placed in a correct position.\n
A White Indicator Peg shows if a correct color is used but in an incorrect position.\n 
A Blank shows if an incorrect color is guessed. \n
\n
You have up to 10 rounds to correctly guess the secret code.\n
\n
if you're ready to guess, press (G)! If you'd like to exit, press (E).
			"""
)
		if rules_menu_input.lower == "G":
			input_guess()
		elif rules_menu_input.lower == "E":
			show_exit()
		else:
			print("I didn't quite understand, please try again.")
			show_rules()

	
	def show_start(self):
		"""Include an option to see the rules at any time during game play. Calls the show_rules method."""
		start_input = input(

"""Welcome to...
 /     \\ _____    _______/  |_  ___________  _____ |__| ____    __| _/
 /  \\ /  \\\\__  \\  /  ___/\\   __\\/ __ \\_  __ \\/     \\|  |/    \\  / __ | 
/    Y    \\/ __ \\_\\___ \\  |  | \\  ___/|  | \\/  Y Y  \\  |   |  \\/ /_/ | 
\\____|__  (____  /____  > |__|  \___  >__|  |__|_|  /__|___|  /\____ | 
        \\/     \\/     \\/            \\/            \\/        \\/      \\/ 
If you'd like to play, press (S). If you'd like to exit, press (E).""")


		if start_input.lower() == "S":
			print(show_rules)

		elif start_input.lower() == "E":
			print("Sad to see you go! Goodbye.")
			exit()
		else:
			print("That is not a valid input.")

		pass
	
	def show_win(self):
		"""display to user when user wins"""
		print("Congratulations, you've won!")
	
	def show_lose(self):
		"""display to user when user loses"""
		print("""oooooohhhhhh, \n 
			You loose\n
			go have an espresso and try agian.....\n""")
	
	def show_exit(self):
		"""display to user when exit option is selected at any point in the game."""
		print("OK, hate to see you go, but if that is the way it needs to be ........")
		#add a pause here 
		exit()
	
	def input_guess(self):
		"""receives input from user to create their guess for each round"""
		guess_input = input("""Please pick the four colors you'd like to guess for this round. 
Your color options are: "Blu" for Blue, "B" for Black, "Y" for Yellow, "R" for Red, "G" for Green, and "W" for White.
Remember: Type them in the order of your guess with a comma between each color.""")
		# This list is passed to the controller and used in Guess
		# guess_input = "blu,b,Y,r"
		return guess_input







