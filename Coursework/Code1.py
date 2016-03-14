import random
import os
import time

continue1 = True

def Roll(sides):
	if sides == 4 or sides == 6 or sides == 12:
		number = random.randint(1,sides)
		print ("I rolled a", sides, "sided dice, and got", number)
	else:
		print ("You can't roll that number!")

while continue1 == True:
	sides = input("Pick a 4,6 or 12 sided dice to roll: ")
	if sides.isdigit() == True:
		sides = int(sides)
		Roll(sides)
		continue2 = (input("Would you like to continue: ").lower())
		os.system('cls')
		if continue2 != "yes":
			print ("Bye!")
			continue1 = False
	else:
		print ("Thats not a number!")
		time.sleep (2)
		os.system('cls')
