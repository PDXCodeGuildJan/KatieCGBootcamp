from creature import Creature

class Monster(Creature):

	AGRO = "agressive"
	DEFENSE = "defensive"

	def __init__(self):
		super.__init__(self)
		self.personality = AGRO

		

