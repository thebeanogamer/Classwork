import random
import os

while True:
	answer = random.randint(1,100)
	print ("In this game you have to guess the whole number, between 1 and 100!")
	while True:
		guess = int(input("Guess the number: "))
		if guess == answer:
			print("You got it right")
			input("Hit enter to start again")
			os.system("cls")
			break
		elif answer > guess:
			print("Too low, try again")
		elif answer < guess:
			print ("Too high, try again")
