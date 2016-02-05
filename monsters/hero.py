from creature import Creature
from monster import Monster

class Hero(Creature):

	def __init__(self):

		super(Hero, self).__init__()
		self.level = 1

# Creates MonsterHero class that inherits properties from Monster and Hero classes
class MonsterHero(Monster, Hero):
	"""The class MonsterHero inherits both Monster and Hero
		classes. Any creature created with the MonsterHero class 
		will now have attributes from both Monster and Hero classes."""

	def __init__(self):
		# Takes this instance(self) of Monster and adds all init properties from Monster class
		Monster.__init__(self)
		# Takes this instance(self) of Monster and adds all init properties from Monster class
		Hero.__init__(self)
		#MonsterHero to have a second weapon
		self.second_weapon = "second weapon!"

