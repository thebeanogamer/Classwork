while True:
	value = int(input("Enter a number: "))
	if value < 20:
		print("Too small!")
	elif value == 54:
		print("You found the secret!")
	elif value > 50:
		print("Too big!")
