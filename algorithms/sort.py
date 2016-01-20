""" A series of various sort algorithm Implementations. 
	selection
	insertion
	bubble
	Author: Katie Dover
"""

def main():

	finished_sorted_list = selection_sort([1, 5, 10, 2, 7])
	print(finished_sorted_list)

	sorted_list = bubble_sort([7, 23, 13, 10, 4, 394])
	print(sorted_list)

	sorted_list = insertion_sort(["K", "C", "D", "H", "P", "G", "S"])
	print(sorted_list)

	sorted_list = merge_sort([3, 5, 20, 13, 7, 30, 394])
	print(sorted_list)
# Make a function that sorts numbers from lowest to highest
# then return the list of numbers in numerical order


# Define selection_sort with the intention of creating my_list

# Implement a selection sort
# Returns: a completed list of numbers from < to > using selection sort
def selection_sort(my_list):

	# The loop will go through each unsorted number in the list looking for the smallest number
	for num in range(len(my_list)):
		lowest_position = num
		current_position = num 
		while len(my_list) > current_position:
			if my_list[lowest_position] > my_list[current_position]:
				lowest_position = current_position	
			current_position += 1

		# swap lowest num into first position
		# three lines of code

		# Give the smallest number to a new variable
		holding_cell = my_list[lowest_position]
		# Swap the number in the spot awaiting the smallest number to the spot where the smallest number was
		my_list[lowest_position] = my_list[num]
		# Take the smallest number from new variable and put it into the spot we just swapped
		my_list[num] = holding_cell



	return my_list



###########NOTES FOR SELECTION SORT################
#the loop will go through each unsorted number in the list looking for the smallest number
	
#If an unsorted number in the list is smaller than the smallest unsorted number found thus far,

#the loop will track the new smallest number
#Once the list has been processed and the numbers have all checked,
#the smallest number will swap to the first spot of the unsorted list

#Update the start of the unsorted list to be the next spot

#the loop will repeat this process until the unsorted list is empty.


#return new sorted list from smallest to largest


###########END OF NOTES FOR SELECTION SORT###########

#####################################################

# Implements a bubble sort algorithm
# Returns a completed list of numbers, sorted from < to > using bubble sort
def bubble_sort(my_list):
	
	finished = False

	while not finished:
		finished = True
		current_index = 0
		next_index = 1
		while current_index < len(my_list) -1:

			if my_list[current_index] > my_list[next_index]:
			# Put the smallest number into a holding cell
				holding_cell = my_list[current_index]
			# Swap the number in the spot awaiting the smallest number
			# to the spot where the smallest number was
				my_list[current_index] = my_list[next_index]
			# Take the smallest number from new variable and put it into the spot we just swapped
				my_list[next_index] = holding_cell
				finished = False

			current_index += 1
			next_index += 1

	return my_list



#####################################################

###########START OF NOTES FOR BUBBLE SORT#############

#every iteration of the list requires one less check, as larger items naturally "sink" to the 
#bottom and smaller items "bubble" to the top

#objective:
#Make a loop that will go through each unsorted number in a list looking for the lowest number
#After going through the entire list, print out the now sorted list from highest to lowest

######

#compare two adjacent numbers in the unordered list in the order they appear

#swap their position if the smallest number of the two is on the left
#don't swap their position if the smallest of the two is on the right

#print out the new sorted list with the numbers ordered from highest to lowest

###########END OF NOTES FOR BUBBLE SORT#############



####################################################

# Swaps two items in a list
# Returns: the list with two things swapped
def swap(my_list, index_a, index_b):

	# Make a temporary variable to hold one value
	temp_holder = my_list[index_a]

	# Swap the values
	my_list[index_a] = my_list[index_b]
	my_list[index_b] = temp_holder

	# Return list with swapped items
	return my_list

#####################################################

#####################################################

# Make an insertion sort function
# Return a list of numbers from < to > using the insertion sort
#	algorithm
def insertion_sort(my_list):

	for start_index, value in enumerate(my_list):
		#lost_index is the number that needs a home
		#and needs sorting
		#make a temp var for the INDEX of teh thing
		#we're currenting sorting
		lost_index = start_index
		lost_value = value

		# look for where the lost index's value belongs
		while (lost_value < my_list[lost_index -1]
				and lost_index > 0):

		#Swap the lost value with it's adjacent value
			my_list = swap(my_list, lost_index, lost_index-1)

			#Decrement te lost_index
			lost_index -= 1


	return my_list

#####################################################

#####################################################

# Implement a merge sort algorithm using recursive functions

def merge_sort(my_list):
	"""Implement the merge sort algorithm"""
	
	if len(my_list) > 1:
		start = 0 
		mid = len(my_list) // 2
		end = len(my_list)

		# Split numbers into two halves
		# First_sorted = list from start to mid point
		# Second_sorted = list from mid point to end
		first_sorted, second_sorted = my_list[start:mid], my_list[mid:end]

		# Sort the first half using merge_sort
		first_sorted = merge_sort(first_sorted)

		# Sort the second half using merge_sort
		second_sorted = merge_sort(second_sorted)

		# Merge the two sorted halves back together
		my_list = merge(first_sorted, second_sorted)

		# Return the merged, sorted list
	return my_list

def merge(list_1, list_2):
	"""Given two lists, merge them together into a third list,
	which is sorted."""
	
	#the indexes will bump +1 each time the function is called
	index_1 = 0
	index_2 = 0
	index_destination = 0
	# list_1 = first_sorted
	numbers_1 = len(list_1)
	# list_2 = second_sorted
	numbers_2 = len(list_2)
	list_destination = [None] * (numbers_1 + numbers_2)
	# While the index number1 is less than the first half of the list (numbers_1)
	#	and the index number2 is less than the second half of the list (numbers_2) 
	while index_1 < numbers_1 and index_2 < numbers_2:
		
		# If the current index of list one is less than the current index of list two
		if list_1[index_1] < list_2[index_2]:
			# The current index of list dest. is now = to the current index of numbers_1
			list_destination[index_destination] = list_1[index_1]
			# Bump up index_destination
			index_destination += 1
			# Bump up index_1
			index_1 += 1

		else: 
			# The current index of list. destination is now = to the current index of list_2
			list_destination[index_destination] = list_2[index_2]
			# Bump up index_destination
			index_destination += 1
			# Bump up index_2
			index_2 += 1

	# If applicable:
	# Take any leftover numbers from the end of index_1 and insert them into the final list_destination
	while index_1 < numbers_1:
		# The index of list_des is now = to the index of list_1
		list_destination[index_destination] = list_1[index_1]
		# Bump up index_destination
		index_destination += 1
		# Bump up index_1
		index_1 += 1
	# If applicable:
	# Take any leftover numbers from index_2 and insert them into the final list_destination
	while index_2 < numbers_2:
		# The index of list_des is now = the index of list_2 
		list_destination[index_destination] = list_2[index_2]
		# Bump up index_destination
		index_destination += 1
		# Bump up index_2
		index_2 += 1

	return list_destination

#####################################################

#####################################################

# If main() is called at the end, and you want to import certain functions inside a module into
# another module, you need to add:
# if __name__ == "__main__":
# to the bottom of the code above main() in the module you're importing.
# example:
if __name__ == "__main__":
	main()
# Make sure main() is indented underneath the if statement

#####################################################
