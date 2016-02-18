""" Linked list implementation
Create a module that:
A. Searches a linked list by value
B. Adds new nodes to the end of a Linked list
C. Removes nodes from anywhere inside a Linked List """

__author__ = "Katie Dover"

def main():
   link = LinkedList()
   link.add(4)
   link.add(2)
   link.add(86)
   link.add(4)
   link.add(7)
   print("Current list:", link)
   link.remove(4)
   print("List after first 4 is removed:", link)
   link.remove(4)
   print("List after second 4 is removed:", link)
   print("Success! Attempt to remove a third 4 yielded no crashes!")
   link.remove(4)
   
   # Output of above code:
   # -------------------------
   # Current list: 4 2 86 4 7 
   # List after first 4 is removed: 2 86 4 7 
   # List after second 4 is removed: 2 86 7 
   # Attempt to remove a third 4 yielded no crashes

class Node:

	def __init__(self, value):
		self.value = value
		self.next_node = None
	
	def __str__(self):
		return str(self.value)

class LinkedList:

	def __init__(self):
		self.head = None


	def search(self, value):
		""" Search a linked list by value."""
		pass

	def add(self, value):
		""" Add a node to the end of the Linked List."""
		# Create node to be added to end of Linked List
		new_node = Node(value)
		
		# If the there is no head (or no Linked list)
		if self.head == None:
			# Create head
			self.head = new_node 
		# If there is an existing head in the LL:
		else:
			# the current node is now the head
			current_node = self.head
			# While the next node in current node does not = None:
			while current_node.next_node != None:
				current_node = current_node.next_node

			# Append it to the end of existing Linked List
			current_node.next_node = new_node

	
	def remove(self, value):
		""" Remove a node from anywhere inisde the Linked List
			and re-link new list. """

		# Take already existing node(s) created by add() and remove them from the Linked List
		# Create current node, previous node, and the one you're searching
		curr_node = self.head
		prev_node = None
		node_search = False
		#Loop (or search) through the linked list to find the node to remove
		while curr_node and node_search is False:
			# If the node we're searching for is in the list
			# node_search is now True

		# If the curr_node is None:
			# The value is not in the list

		### End of exercise thoughts### 

		# Like I explained in the code, I needed to loop through the linked list to locate
		# the node to remove, assign the previous node to the node located directly after
		# The node to remove, and remove the node. 
		# In the while loop, I needed to loop through the LL to find the node to search for 
		# 

		###  ###


		# Logic: 
		# Because nodes always need something to point to...
		# To remove b:
		# First get A point to what B is pointing to- C.

		# A's pointer will now point to C(no longer B), B is still pointing to C

		# Once A is pointing to C

		# We can now remove B! A is still A, C is now B, D is now C, and so on and so forth. 

	def __str__(self):	
		temp_list = []
		current_node = self.head

		while current_node:
			temp_list.append(current_node.value)
			current_node = current_node.next_node
			

		return str(temp_list)
		

		



if __name__ == '__main__':
	main()




