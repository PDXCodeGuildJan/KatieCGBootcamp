from creature import Creature

class Monster(Creature):

	AGGRO = "agressive"
	DEFENSE = "defensive"

	def __init__(self):
		# We pass Monster because super represents Creature, Monster represents Monster.
		super(Monster, self).__init__()
		self.personality = Monster.AGGRO



