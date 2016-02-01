def main():
	#can be changed to any string
	string = "Katie Is Cool"
	#calls the mid3 function below, carries string 
	middle_three_characters(string)

	my_list = ["Mr", "and", "Mrs", "Dursley", "of" "number", "4", "Privet", "Drive"]
	sequence_printer(my_list)

def middle_three_characters(string):
	#finds the middle of the string
	mid = (len(string)-3)//2
	#finds the two letters surrounding it
	print(string [mid:mid+3])

	sequence_printer(string)



def sequence_printer(string):
	print(string)
	for x in string:
		print(x)

main()



# 	the_string = len(string_practice)
# 	print(the_string)

# middle_characters(the_string)

#length divided by two, plus one on either side 