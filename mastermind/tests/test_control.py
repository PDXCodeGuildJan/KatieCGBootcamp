__author__ = "Gabriel Key", "Katie Dover"

import unittest

from mm_control import MasterMind

class RoundAdvanceTest(unittest.TestCase):


	def setUp(self):

		self.master = MasterMind()



	def tearDown(self):
		del self.master


	def test_round_advance(self):

		# set the current round to 2
		level = self.master.model.status + 1

		self.master.round_advance()

		self.assertEqual(level, self.master.model.status, "levels do not match")



class WinCheckTest(unittest.TestCase):

	"""we will come back to this"""

	pass


class CheckStatustest (unittest.TestCase):

	def setUp(self):
		self.master = MasterMind()


	def tearDown(self):
		del self.master

	def test_check_status(self):

		# set current round to 10 or greater
		self.master.model.status = 10

		self.assertEqual(False, self.master.check_status(), "if level is 10 or greater, user receives prompt loose")		




		# set the current round to 9 or lower
		self.master.model.status = 9

		self.assertEqual(True, self.master.check_status(), "if level is 9 or lower prompt you loose")










