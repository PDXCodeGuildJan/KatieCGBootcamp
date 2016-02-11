""" Linked list implementation
Create a module that:
A. Searches a linked list by value
B. Adds new nodes to the end of a Linked list
C. Removes nodes from anywhere inside a Linked List """

__author__ = "Katie Dover"


class Node:

	def __init__(self, value):
		self.value = value
		self.next_node = None
	
	def __str__(self):
		return str(self.value)

class Linked_List:

	def __init__(self):
		self.head = None

	def search(self, value):
		""" Search a linked list by value."""
		pass

	def add(self, value):
		""" Add a node to the end of the Linked List."""
		# Create node to be added to end of Linked List
		new_node = Node(value)
		
		if self.head == None:
			self.head = new_node 
		# Find end of linked list
		else:
			current_node = self.head
			while current_node.next_node != None:
				current_node = current_node.next_node

			# Append it to the end of existing Linked List
			current_node.next_node = new_node

	def __str__(self):	
		temp_list = []
		current_node = self.head

		while current_node:
			temp_list.append(current_node.value)
			current_node = current_node.next_node
			

		return str(temp_list)
		

	def remove(self, value):
		""" Remove a node from anywhere inisde the Linked List
			and re-link new list. """
		pass



my_list = Linked_List()

my_list.add("Item 1")
my_list.add("Item 2")
my_list.add("Item 3")
my_list.add("Item 4")
print(my_list)




