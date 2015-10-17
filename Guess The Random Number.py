import random
import os
import sys

while True:
	againhuman = ""
	times = 0
	answer = random.randint(1,100)
	print ("In this game you have to guess the whole number, between 1 and 100!")
	while True:
		guess = int(input("Guess the number: "))
		if guess == answer:
			times = times + 1
			print("You got it right, and it took you",times, "goes")
			againhuman = input("Go again? ")
			if againhuman == "yes" or againhuman == "Yes":
				input("Hit enter to start again")
				os.system("cls")
			else:
				sys.exit()
			break
		elif answer > guess:
			times = times + 1
			print("Too low, try again")
		elif answer < guess:
			times = times + 1
			print ("Too high, try again")
