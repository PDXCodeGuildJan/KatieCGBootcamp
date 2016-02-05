from creature import Creature
from monster import Monster

class Hero(Creature):

	def __init__(self):

		super(Hero, self).__init__()
		self.level = 1


class MonsterHero(Monster, Hero):

	def __init__(self):
		Monster.__init__(self)
		Hero.__init__(self)
		self.second_weapon = "second weapon!"

	#Monster Hero to have a second weapon