



class MasterView:


	def show_curr_guess():
		"""displays the current guess, is a part of big display"""
		pass

	def show_past_guess(guess_response):
		"""shows players past guesses"""
		pass
	
	def show_status(eval_status):
		""" shows players current status a.k.a. round """
		pass
	
	def show_pegs(guess_response):
		"""shows black and white pegs as part of big display"""
		pass
	
	def show_solution(color_picker):
		"""shows colors chosen as part of color_picker to player at end of game, exit, or win. """
		pass
	
	def show_rules():
		"""Shows the user all Mastermind rules at any time during game play."""
		pass
	
	def show_start():
		"""Include an option to see the rules at any time during game play. Calls the show_rules method."""
		start_input = input(

"""Welcome to...
 /     \ _____    _______/  |_  ___________  _____ |__| ____    __| _/
 /  \ /  \\__  \  /  ___/\   __\/ __ \_  __ \/     \|  |/    \  / __ | 
/    Y    \/ __ \_\___ \  |  | \  ___/|  | \/  Y Y  \  |   |  \/ /_/ | 
\____|__  (____  /____  > |__|  \___  >__|  |__|_|  /__|___|  /\____ | 
        \/     \/     \/            \/            \/        \/      \/ 
If you'd like to play, press (S). If you'd like to exit, press (E).""")
		if start_input == "S":
				print("LIST ALL OF THE RULES HERE.")

		elif start_input == "E":
			print("Sad to see you go! Goodbye.")
			exit()
		else:
			print("That is not a valid input.")



		pass
	
	def show_win():
		"""display to user when user wines"""
		pass
	
	def show_lose():
		"""display to user when user looses"""
		pass
	
	def show_exit():
		"""display to user when exit option is selected at any point in the game."""
		pass
	
	def input_guess():
		"""receives input from user to create their guess for each round"""
		pass
	
	def big_display(show_past_guess, show_status, show_pegs, show_curr_guess):
		"""combines all above infomation into cohsieve display to user."""
		pass





