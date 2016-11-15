punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~£'''
# Creates the list of punctuation to remove
no_punct1 = ""
# Creates the string to contain the punctuation free inpu
wordschecked = 0
# Monitors the word being edited
finalwords = []
# Creates the array for the words
finalnumbers = []
# Creates the array for the numbers

String = str(input("What is your string? ").lower())
# Gets the user's input
while String == "":
	print("Umm, no. I need something to work with!")
	String = input("What is your string? ").lower()
	# Repeats the question until a string is inputted
for char in String:
	if char not in punctuation:
		no_punct1 = no_punct1 + char
		# Creates a new string containing only characters not in the punctuation list
no_punct1 = no_punct1.split()
# Breaks the input down into an array
while wordschecked != len(no_punct1):
	# Runs for an amount of times equivalent to the length of the string
	if any(no_punct1[wordschecked] in s for s in finalwords):
		# Checks if the word is already in the array
		finalnumbers.append(finalwords.index(no_punct1[wordschecked]))
		# Adds the number corresponding to the position in the words array to the numbers array
	else:
		finalnumbers.append(wordschecked)
		# Adds the current word number to the numbers array
		finalwords.append(no_punct1[wordschecked])
		# Adds the current word to the words array
	wordschecked = wordschecked + 1
	# Goes to the next word in the array
print (finalwords)
print (finalnumbers)
# Prints the arrays for debugging
wordsfile = open("words.txt",'w')
numbersfile = open("numbers.txt", 'w')
# Opens the text files
wordsfile = wordsfile.write(str(finalwords))
numbersfile = numbersfile.write(str(finalnumbers))
# Writes the arrays to the files
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~£'''
# Creates the list of punctuation to remove
no_punct1 = ""
# Creates the string to contain the punctuation free inpu
wordschecked = 0
# Monitors the word being edited
finalwords = []
# Creates the array for the words
finalnumbers = []
# Creates the array for the numbers

String = str(input("What is your string? ").lower())
# Gets the user's input
while String == "":
	print("Umm, no. I need something to work with!")
	String = input("What is your string? ").lower()
	# Repeats the question until a string is inputted
for char in String:
	if char not in punctuation:
		no_punct1 = no_punct1 + char
		# Creates a new string containing only characters not in the punctuation list
no_punct1 = no_punct1.split()
# Breaks the input down into an array
while wordschecked != len(no_punct1):
	# Runs for an amount of times equivalent to the length of the string
	if any(no_punct1[wordschecked] in s for s in finalwords):
		# Checks if the word is already in the array
		finalnumbers.append(finalwords.index(no_punct1[wordschecked]))
		# Adds the number corresponding to the position in the words array to the numbers array
	else:
		finalnumbers.append(wordschecked)
		# Adds the current word number to the numbers array
		finalwords.append(no_punct1[wordschecked])
		# Adds the current word to the words array
	wordschecked = wordschecked + 1
	# Goes to the next word in the array
print (finalwords)
print (finalnumbers)
# Prints the arrays for debugging
wordsfile = open("words.txt",'w')
numbersfile = open("numbers.txt", 'w')
# Opens the text files
wordsfile = wordsfile.write(str(finalwords))
numbersfile = numbersfile.write(str(finalnumbers))
# Writes the arrays to the files
