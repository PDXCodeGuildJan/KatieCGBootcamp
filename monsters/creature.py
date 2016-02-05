"""Dungeon crawler game"""



class Creature:
	"""Makes a class for creatures. All creatures and heroes played in
		the game will be made from this class. They all come with a name,
		stats, special abilities, and a weapon."""

	# Constants for the states of all creatures
	NORMAL = "normal"
	ASLEEP = "asleep"
	UNCONS = "unconscious"
	POISONED = "poisoned"
	WEAKENED = "weakened"

	def __init__(self):
		"""Initializes all stats for every creature to be created in the
			game."""
		self.name = ""
		self.state = Creature.NORMAL
		self.stats = {}
		self.health = 20
		self.max_health = 20
		self.attack_points = 2
		self.weapon = None
		self.special_abilities = {} #special abilities
	

	def attack(self):
		""""""
		pass

	def heal(self, heal_amount):
		""""""
		pass

	def defend(self, attack_amount):
		""""""
		pass

	def take_damage(self, damage):
		""""""
		pass

	def change_weapon(self, new_weapon):
		""""""
		pass

	def change_state(self, new_state):
		""""""
		pass
