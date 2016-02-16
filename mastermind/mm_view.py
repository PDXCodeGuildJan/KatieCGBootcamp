



class MasterView:


	def show_curr_guess():
		pass

	def show_past_guess(guess_response):
		pass
	
	def show_status(eval_status):
		pass
	
	def show_pegs(guess_response):
		pass
	
	def show_solution(solution_picker):
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
		pass
	
	def show_lose():
		pass
	
	def show_exit():
		pass
	
	def input_guess():
		pass
	
	def big_display(show_past_guess, show_status, show_pegs, show_curr_guess):
		pass