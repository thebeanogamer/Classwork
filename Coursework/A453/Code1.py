import os
# Imports OS to make terminal clear possible

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~£'''
# Creates list of all punctuation to replace

Continue = True
# Causes the while loop to run

while Continue == True:
	# Ensures program will run until told otherwise
	x = 0
	# Used to monitor position in string
	Present = False
	# Creates a failsafe in case the string is not present
	String = input("What is the string: ").lower()
	# Asks the user to input a string
	no_punct1 = ""
	no_punct2 = ""
	# Creates empty variables to store punctuation free strings
	for char in String:
		# Repeats for every character in the string
		if char not in punctuations:
			# Only runs if the character is not punctuation
			no_punct1 = no_punct1 + char
			# Adds the character to the punctuation free string
	no_punct1 = no_punct1.split()
	# Breaks the punctuation free string for easier searching
	Term = input("What is the search term: ").lower()
	# Asks the user to input a search term
	for char in Term:
		# Repeats for every character in the term
		if char not in punctuations:
			# Only runs if the character is not punctuation
			no_punct2 = no_punct2 + char
			# Adds the character to the punctuation free string
	while x != len(no_punct1):
		# Runs for every word in the string
		if no_punct2 == no_punct1[x]:
			# Checks if the word is that which it is looking for
			print("Word", (x + 1))
			# Informs the user of its discovery
			Present = True
			# Saves that the string is present at least once
		x = x + 1
		# Causes the program to repeat
	if Present == False:
		# Checks if the term ever appeared
		print ("Term not present!")
		# Informs the user of its discovery
	ContinueRaw = input("Continue Y/N ").lower()
	# Asks the user if they want to repeat
	if ContinueRaw == "n":
		# If the user does not want to the loop will stop and the program will end
		Continue = False
	else:
		os.system('cls')
		# Clears the screen and starts the loop again
