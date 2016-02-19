"""Dungeon crawler game"""

class Weapon:
	"""Weapon objects that creatures can equip."""
	def __init__(self, atk_value):
		self.base_damage = atk_value


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
		"""Return the attack value of of the creature, given its 
		base attack value, Weapon attack value, and state."""
		# Set the attack value to the base attack amount
		atk_value = self.attack_points
		# If we have a weapon, add the weapon's damage to atk_value
		if self.weapon:
			atk_value += self.weapon.base_damage

		# Return the total calculated damage
		return atk_value

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

