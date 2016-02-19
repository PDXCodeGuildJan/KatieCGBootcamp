__author__ = "Katie Dover"

import unittest
# Import the class where the function lives that you're testing
from creature import Creature, Weapon

# Make a new TestCase, CreateAttackTest,
# which inherits from unittest.TestCase
class CreatureAttachTest(unittest.TestCase):

	# Make the things and do the setup that every test 
	# in the TestCase need.
	def setUp(self):
		"""Create an instance of the Creature class that we 
		can leverage it's functions in our tests.
		"""
		self.creature = Creature()

	# Undos everything that your setUp function did
	def tearDown(self):
		"""Delete the Creature instamce we made in the setUp.
		"""

		del self.creature

	def test_attack_return_int(self):
		"""Ensure that when attack is called, an int is returned.
		"""
		# Call the attack function of our creature,
		# and catch what it returns in value.
		value = self.creature.attack()


		self.assertIsInstance(value, int, "Returned attack value is not an int")

	
	def test_no_weapon_return_base_damage(self):
		"""Ensure that with no weapon equipped, the creature does its 
		base damage.
		"""
		# Manually set the base damage to 2 
		self.creature.attack_points = 2

		# Get the creature's attack value
		value = self.creature.attack()

		self.assertEqual(value, 2, "Expected base attack value not given")

	def test_with_weapon_return_damage(self):
		"""Ensure that with a weapon, the creature does base damage + weapon
		damage. 
		"""
		# Make a weapon to give to the creature
		weapon = Weapon(3)

		# Give the weapon to the creature
		self.creature.weapon = weapon

		# Set the creature's base attack value
		self.creature.attack_points = 2

		# Get the creature's total attack value
		value = self.creature.attack()
		# Assert the attack value is the base + weapon damage
		self.assertEqual(value, 5, "Computed attack value is not correct.")


		









