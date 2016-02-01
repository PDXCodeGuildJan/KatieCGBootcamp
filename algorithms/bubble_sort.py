my_list = (1, 5, 8, 3, 2, 20)

def bubble_sort(my_list):

	for num in range(len(my_list)):
		lowest_position = num
		current_position = num 
		
		#would we need to track both numbers/positions?????
		while len(my_list) > current_position:
			if my_list[lowest_position] < my_list[current_position]:
				lowest_position = current_position
			current_position -1

	return my_list
	print(my_list)


bubble_sort(my_list)