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

	

