import sys

while True:
	height = input('How tall should the tree be (3-20)? You can write "exit" to stop. ')
	x = 0

	if height.isdigit():
		#Checks if the input is a number
		height = int(height) + 1
		#Converts height to a intger
		if height > 3 and height <= 21:
			while x < height:
				print ("*" * x)
				x = x + 1
		else:
			print ("No, thats not what I asked for. Read it again!")
			print ()
	elif height == "exit":
		sys.exit()
	else:
		print("Thats not a number, make sure you write it in digits!")
