def practice_work():
	#can be changed to any string
	string = "Dumbledore!"
	#calls the mid3 function below, carries string 
	middle_three_characters(string)

def middle_three_characters(string):
	#finds the middle of the string
	mid=(len(string)-3)//2
	#finds the two letters surrounding it
	print(string [mid:mid+3])

	sequence_printer(string)



def sequence_printer(string):
	print(string)
	for x in string:
		print(x)

practice_work()



# 	the_string = len(string_practice)
# 	print(the_string)

# middle_characters(the_string)

#length divided by two, plus one on either side 