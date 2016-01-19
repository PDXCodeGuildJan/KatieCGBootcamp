#Make a function that sorts numbers from lowest to highest
#then return the list of numbers in numerical order


#Define selection_sort with the intention of creating the_list
def selection_sort(my_list):

	#the loop will go through each unsorted number in the list looking for the smallest number
	for num in range(len(my_list)):
		lowest_position = num
		current_position = num 
		#while """the number we're checking""" is > """than the lowest number in in sorted_list but""" < """ and all the numbers in unsorted_list""":
			#"""put that number in the next available spot of the sorted_list """
		while len(my_list) > current_position:
			if my_list[lowest_position] > my_list[current_position]:
				lowest_position = current_position	
			current_position += 1

		#swap lowest num into first position
		#three lines of code

		#Give the smallest number to a new variable
		holding_cell = my_list[lowest_position]
		#Swap the number in the spot awaiting the smallest number to the spot where the smallest number was
		my_list[lowest_position] = my_list[num]
		#take the smallest number from new variable and put it into the spot we just swapped
		my_list[num] = holding_cell



	return my_list

finished_sorted_list = selection_sort([1, 5, 10, 2, 7])
print(finished_sorted_list)

	###########NOTES FOR SELECTION SORT#############
		#the loop will go through each unsorted number in the list looking for the smallest number
	
	#If an unsorted number in the list is smaller than the smallest unsorted number found thus far,


	


	#the loop will track the new smallest number
	#Once the list has been processed and the numbers have all checked,
	#the smallest number will swap to the first spot of the unsorted list

	#Update the start of the unsorted list to be the next spot

	#the loop will repeat this process until the unsorted list is empty.

	
	#return new sorted list from smallest to largest
	############
	#return the_list
	############



#sorted = selection_sort([1, 5, 10, 2, 7])
#print(sorted)


	###print(the_list)
###########END OF NOTES FOR SELECTION SORT#############


def bubble_sort(my_list):
	
	finished = False
	
	while not finished:
		finished = True
		current_index = 0
		next_index = 1

		while current_index < len(my_list) -1:

			if my_list[current_index] > my_list[next_index]:
				holding_cell = my_list[current_index]
			#Swap the number in the spot awaiting the smallest number to the spot where the smallest number was
				my_list[current_index] = my_list[next_index]
			#take the smallest number from new variable and put it into the spot we just swapped
				my_list[next_index] = holding_cell
				finished = False

			current_index += 1
			next_index += 1

	return my_list

sorted_list = bubble_sort([7, 23, 13, 10, 4, 394])
print(sorted_list)



			
			#would we need to track both numbers/positions????




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

