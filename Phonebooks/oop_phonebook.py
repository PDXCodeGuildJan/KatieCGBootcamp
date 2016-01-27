"""A phonebook program implemented with Classes."""

__author__ = "Katie Dover"

class Contact:
	"""Defines the Contact object to store information about people."""

	def __init__ (self, f_name, l_name):
		# Assign passed arguments to their corresponding properties
		self.first_name = f_name
		self.last_name = l_name

		self.phone_num = ""
		self.addresses = {}
		self.email = ""

	def update_address(self, addy_key, street=None, unit=None,
						city=None, state=None, zip_code=None, country=None):
		"""Update addy_key with the information passed"""
		
		if addy_key in self.addresses:
			temp_address = self.addresses[addy_key]
		else: 
			# Make a new address object
			temp_address = Address()
		# Set the new address' stree to whatever was passed
		if street:
			temp_address.street = street
		if unit:
			temp_address.unit = unit
		if city:
			temp_address.city = city
		if state:
			temp_address.state = state
		if zip_code:
			temp_address.zip_code = zip_code
		if country:
			temp_address.country = country
		# Assign the address to the given address key for the Contact
		self.addresses[addy_key] = temp_address



	def format_phone_num(self, phone_num):
		"""Format the phone number of the contact all pretty-like."""
		regex = "[0-9]+"
		nums = re.findall(regex, phone_num)
		# Take everything in the list of numbers and make it into a string of nums
		new_num = ""
		for every_number in nums:
			new_num += every_number

		# Introduce the correct formatting
		formatted_num = "(" + new_num[0:3] + ")" + new_num[3:6] + "-" + new_num[6:]

		# Save formatted number to Contact
		self.phone_num = formatted_num

	def __str__(self):
		"""Print out the contact's info, all pretty-like."""
		# Initialize formatted string 
		formatted_string = "Name: {0} {1}".format(self.first_name, self.last_name)

		# If there is a phone number
		if self.phone_num:
			# Format the phone number all pretty
			self.format_phone_num(self.phone_num)
			# Add the pretty phone number to the formatted_string
			formatted_string += "\nPhone: {0}".format(self.formatted_num)
		# If there is an email address
		if self.email:
			formatted_string += "\nEmail: {0}".format(self.email)

		# If there are any addresses

		if self.addresses:
			formatted_string += "\nAddress(es):"
			formatted_string += "\n--------------------------------"
			# Loop through all addresses and print them
			# Get all the key, value pairs of the addresses using te Dictionary.items function
			for key, address in self.addresses.items():
				formatted_string += "\n{0}".format(key)
				formatted_string += "\n{0}".format(address)
				formatted_string += "\n------------------"

		return formatted_string

class Address:
	"""Defines the address object to be used with Contact."""

	def __init__ (self):
		self.street = ""
		self.unit = ""
		self.city = ""
		self.state = ""
		self.zip_code = ""
		self.country = ""

	def __str__(self):
		"""Print out address formatted all pretty-like."""
		
		formatted_string = self.street
		if self.unit != "":
			formatted_string += "\n" + self.unit

		formatted_string += "\n" + self.city + " " + self.state
		formatted_string += " " + self.zip_code
		formatted_string += "\n" + self.country

		return formatted_string








