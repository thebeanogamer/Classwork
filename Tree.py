import sys

while True:
	height = input('How tall should the tree be (3-20)? You can write "exit" to stop. ')
	x = 0

	if height.isdigit():
		#Checks if the input is a number
		height = int(height) + 1
		#Converts height to a intger
		while height < 3 or height > 20:
			print ("No, thats not what I asked for. Read it again!")
			height = input("How tall should the tree be (3-20)? ")
			break
		while x < height:
			print ("*" * x)
			x = x + 1
	elif height == "exit":
		sys.exit()
	else:
		print("Thats not a number, make sure you write it in digits!")
