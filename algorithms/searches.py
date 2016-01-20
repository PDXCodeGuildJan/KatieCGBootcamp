""" A series of search algorithm implementations.
	Author: Katie Dover
"""

from sort import insertion_sort

def main():
	# Make a list to look through, and the target value
	unsorted_list = ["K", "C", "D", "H", "P", "G", "S"]
	target_value = "P"

	# Call the search function, catch what it returns
	sorted_list, target_index = binary_search(unsorted_list, target_value)

	# Print out our solution
	print(sorted_list, "I found", target_value, "and it's at", target_index)

# Implements the Binary search algorithm
def binary_search(the_list, target_value):

	# First, sort the list
	sorted_list = insertion_sort(the_list)

	length = len(sorted_list)

	# Initialize start and end variables
	start = 0
	end = length

	# while length is >= 1 look for target: 
	while length >= 1:
	# look for target
		# Find the mid point of the segment we're looking in
		mid = start + (length // 2)
		# Determine if middle value is >, <, or equal, 
		# If statement to find out which of the three is true
		# If equal, we found it. Return middle
		if sorted_list[mid] == target_value:
			return (sorted_list, mid)
		# Elif greater than, reduce segment to to left half from middle, repeat loop
		elif sorted_list[mid] > target_value:
			length =len(sorted_list[start:mid])
			end = mid
		# Elif less than, reduce segment to right half from middle, repeat loop
		elif sorted_list[mid] < target_value:
			length = len(sorted_list[mid + 1:end])
			start = mid + 1

	# If we can't find the index, return -1 
	# This return returns the sorted list if the index has been found
	# and -1 if the index wasn't found
	return (sorted_list, -1)

if __name__ == "__main__":
	main()