"""Implements a simple phonebook using a dictionary.
Takes any data given through user input and saves it to
a .txt file.
"""

__author__ = "Katie Dover"

# Imports some cool ass colors because FUN!
import re
from colorama import Fore, Back, Style

# Initializes our dictionary, which will store our phone numbers
phonebook = {}

# Prompts the user to provide a commant to call various functions
def main():
	"""The main driver function of our phonebook"""
	#load any existing data into phonebook
	load_phonebook()

	print(Back.BLACK + "black background")
	print(Fore.GREEN + "-----------------------------------------")
	print("Welcome to your phonebook!")
	print("""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMM8.............88DMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMO...................8DMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMM:.......................8MMMMMMD88~........+D88MMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMD...........................8M8.....................:88MMMMMMMMMM
MMMMMMMMMMMMMM8............................O............................~8MMMMMM
MMMMMMMMMMMMM8............................8.............................+ZMMMMMM
MMMMMMMMMMMM8............................8.............................~,,NMMMMM
MMMMMMMMMMM?............................D.............................=,,,88DMMM
MMMMMMMMMN.............................8.............................?,,,,,8$$$D
MMMMMMMMD.............................8.............................I,,,,,8$$$8M
MMMMMMM8.............................O.............................7,,,,,8$$$8MM
MMMMMMD.............................7.............................Z:,,,,8$$$8MMM
MMMMMI.............................~.............................Z,,,,,8$$$8MMMM
MMMM:=$O888Z7~....................:.............................7,,,,,8$$$8MMMMM
MMM8,,,,,,,,,,,,::88:..........................................$,,,,,8$$$8MMMMMM
MMM8,,,,,,,,,,,,,,,,,,I8.......:..............................$,,,,,8$$$8MMMMMMM
MDO8+$O888O$+,,,,,,,,,,,,=8...7..............................Z,,,,:8$$$8MMMMMMMM
8$$$$$$$$$$$$$$$Z88,,,,,,,,,8O?ZO8OZ7~......................O,,,,:O$$$8MMMMMMMMM
MMMMD888$$$$$$$$$$$$Z8,,,,,,,,,,,,,,,,,,,,=88I.............8,,,,=O$$$8MMMMMMMMMM
MMMMMMMMMMMM888Z$$$$$$$8~I?,,,,,,,,,,,,,,,,,,,,,I8:.......D,,,,?Z$$$8MMMMMMMMMMM
MMMMMMMMMMMMMMMMMMN888$$$$$$$D~,,,,,,,,,,,,,,,,,,,,,8+...8:,,,IZ$$$8MMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMD88Z$$8Z$$$$$Z888~,,,,,,,,,,,,DD,,,,$$$$$8MMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM888$$$$$$$$$$88~,,,,,,,,,,,,O$$$$8MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM888$$$$$$$$OD$,,,,,,,8$$$$8MMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMD88$$$$$$O8I,,8$$$$8MMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM888$$$$8$$$$DMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN88$$ZNMMMMMMMMMMMMMMMMMM
""")
	option = ""
	
	while option != "E":
		# Ask the user what they would like to do.
		option = input("Please choose a command:\n\t(A)dd\n\t(D)elete\n\t(S)earch Contacts by Name\n\tSearch by (N)umber\n\t(P)rint Contacts\n\t(E)xit\nWhich would you like to do?> ")

		if option.upper() == "A":
			print("-----------------------------------------")
			name = input("Please provide the first and last name of your new contact> ")
			number = input("What is " + name + "'s number?> ")
			print("-----------------------------------------")
			add_contact(name, number)

		elif option.upper() == "D":
			print("-----------------------------------------")
			name = input("What contact are you removing?> ")
			print("-----------------------------------------")
			remove_contact(name)

		elif option.upper() =="P":
			print_phonebook()

		elif option.upper() == "S":
			print("-----------------------------------------")
			number = input("Which existing contact are you searching for?> ")
			print("-----------------------------------------")
			search_contact_name(name)

		elif option.upper() == "N":
			print("-----------------------------------------")
			number = input("What number would you like to search for?> ")
			print("-----------------------------------------")
			search_contact_number(number)

		elif option.upper() == "E":
			print("-----------------------------------------")
			print("\tgoodbye!")
			print("-----------------------------------------")
			print(Style.RESET_ALL)
			exit()

		else:
			print("-----------------------------------------")
			print("Invalid input.")
			print("-----------------------------------------")
			main()


def add_contact(name, phonenumber):
	"""Does an addition to a phonebook with the given
		contact info"""

	# Remove any lingering whitespace that might have been added
	# During user input
	regex = "\s+\Z"
	replacement_string = ""
	scrubbed_name = re.sub(regex, replacement_string, name)

	# Scrub and reformat the phone number to follow (XXX) XXX-XXXX pattern
	# Remove all but the numbers
	regex = "[0-9]+"
	nums = re.findall(regex, phonenumber)
	new_num = ""
	for every_number in nums:
		new_num += every_number

	# Introduce the correct formatting
	formatted_num = "(" + new_num[0:3] + ")" + new_num[3:6] + "-" + new_num[6:]


	# Adds contact by adding to the dictionary
	phonebook[scrubbed_name] = formatted_num
	print("-----------------------------------------")
	print("\nNew Contact", scrubbed_name, "was added with number", formatted_num, "\n")
	print("-----------------------------------------")

	# Save updated phonebook
	save_phonebook()
	


def remove_contact(name):
	"""Removes the given contact from the phonebook"""
	# Removes contact from phonebook dictionary
	if name in phonebook:
		del phonebook[name]
		print("-----------------------------------------")
		print("\nYour contact", name, "as been deleted.")
		print("-----------------------------------------")

		# Save updated phonebook
		save_phonebook()
	else: 
		print("-----------------------------------------")
		print("\nsorry,", name, "does not exist.")
		print("-----------------------------------------")
	

def print_phonebook():
	"""Prints every contact in the phonebook in a pretty way."""
	for name in phonebook:
		print("-----------------------------------------")
		print("\nName:", name, "| Number:", phonebook[name], "\n")
		print("-----------------------------------------")

def save_phonebook():
	"""Save the contents of the phonebook to a file."""

	open_file = open("phonebook.txt", "w")
	open_file.write(str(phonebook))
	open_file.close()

def load_phonebook():
	"""load the phonebook data from the save file."""
	# This function has access to change the global val "phonebook"
	global phonebook

	# Open the file in write mode first to create it if it doesn't already exist
	load_file = open("phonebook.txt", "w")
	load_file.close()
	
	# Opening our phonebook.txt file in "read" ("r") mode
	load_file = open("phonebook.txt", "r")
	phonebook_data = load_file.read()
	load_file.close()

	# Convert from string back to dictionary
	phonebook = eval(phonebook_data)

def search_contact_name(name):
	
	result = ""
	for name, number in phonebook.items():
		if name in phonebook:

			number = phonebook[name]
			print("-----------------------------------------")
			print("\n", name, "'s number is", number)
			print("-----------------------------------------")
			result = name
	
		else:
			print("-----------------------------------------")
			print("\nSorry, no contact exists with that name.")
			print("-----------------------------------------")

def search_contact_number(search_number):
	# for key, value in dictionary.items():
	result = ""
	for name, number in phonebook.items():
		if search_number == number:
			print("-----------------------------------------")
			print("\n", name, "'s number is", number, "\n")
			print("-----------------------------------------")
			result = name

	if result == "":
		print("-----------------------------------------")
		print("\nSorry, no contact has that number.")
		print("-----------------------------------------")




if __name__ == '__main__':
	main()