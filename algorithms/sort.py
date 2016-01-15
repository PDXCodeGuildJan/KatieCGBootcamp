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


sorted_list = selection_sort([1, 5, 10, 2, 7])
print(sorted_list)





	



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















"""	unsorted_list = len(the_list)
	sorted_list = len(the_list+1)"""



"""while the_list is > 0 :

			#sorted_list = (len(unsorted_list +1"""




"""
		for lowest_number in the_list:
			lowest_number = unsorted_list"""



"""unsorted_list = len
		sorted_list = len(the_list-1)"""


#unsorted_start = 0
		#while unsorted_start <0: