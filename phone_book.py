"""Implements a very simple phonebook using a dictionary"""

__author__ = "Katie Dover"

#Imports some cool ass colors because FUN!
from colorama import Fore, Back, Style

# Initializes our dictionary, which will store our phone numbers
phonebook = {}

# Prompts the user to provide a commant to call various functions
def main():
	"""The main driver function of our phonebook"""
	print(Back.BLACK + "black background")
	print(Fore.GREEN + "-----------------------------------------")
	print("Welcome to your phonebook!")
	print("""
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
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMM
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

	# Adds contact by adding to the dictionary
	phonebook[name] = phonenumber
	print("-----------------------------------------")
	print("\nNew Contact", name, "was added with number", phonenumber, "\n")
	print("-----------------------------------------")
	


def remove_contact(name):
	"""Removes the given contact from the phonebook"""
	# Removes contact from phonebook dictionary
	if name in phonebook:
		del phonebook[name]
		print("-----------------------------------------")
		print("\nYour contact", name, "as been deleted.")
		print("-----------------------------------------")
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