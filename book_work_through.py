def temp_converter():
	celsius = eval(input("What is the Celsius temperature? "))
	fahrenheit = 9/5 * celsius + 32
	print("The temperature is", fahrenheit, "degrees fahrenheit. :)")

	calculator()


def calculator():
	answer = eval(input("Enter an expression: "))
	print(answer)
	

def fact(n):
	if n == 0:
		return 1 
	else:
		return n *fact(n-1)

