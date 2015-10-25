import sys

while True:
	height = input('How tall should the tree be (3-20)? You can write "exit" to stop. ')
	x = 0

	if height.isdigit():
		#Checks if the input is a number
		height = int(height) + 1
		#Converts height to a intger
		if height > 3 and height <= 21:
			#If the number is whithin the condintions requested then it prints the tree
			while x < height:
				print ("*" * x)
				x = x + 1
		else:
			#If the user inputs a number, but not one requested it reiterates
			print ("No, thats not what I asked for. Read it again!")
			print ()
	elif height == "exit":
		#If the user types exit the program closes
		sys.exit()
	else:
		#If the input is not a number it clarifies
		print("Thats not a number, make sure you write it in digits!")
