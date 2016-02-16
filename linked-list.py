""" Linked list implementation
Create a module that:
A. Searches a linked list by value
B. Adds new nodes to the end of a Linked list
C. Removes nodes from anywhere inside a Linked List """

__author__ = "Katie Dover"


class Node:

	def __init__(self):
	self.value = 0
	self.next_node = None

class LinkedList:

	def __init__(self):
	self.head = Node()


	def search(self, value):
		pass

	def add(self, value):
		""" Add a node to the end of the Linked List."""

	def remove(self, value):
		pass