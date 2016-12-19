Realcommand = False
Command = input("Do you want to encrypt or decrypt? ").lower()
while Realcommand == False:
	#Checks if the command has been verified as real
	if Command == "":
		# Checks if the string is empty
		print ("Um, no. Give me something to work with!")
		Command = input("Do you want to encrypt or decrypt? ").lower()
	elif Command == "encrypt" or Command == "decrypt":
		# Confirms inputted string is real
		Realcommand = True
	else:
		# Repeats the command if the inputted string is not understood
		print ("Um, no. Give me something I understand!")
		Command = input("Do you want to encrypt or decrypt? ").lower()
if Command == "encrypt":
	Wordschecked = 0
	Finalwords = []
	Finalnumbers = []
	Arrayword = 0
	# Create the variables
	String = input("What is your string? ")
	# Gets the user to input a string
	String = String.split()
	# Breaks the inputted string down into an array
	while Wordschecked != len(String):
		# Runs for an amount of times equivalent to the length of the string
		if any(String[Wordschecked] in s for s in Finalwords):
			# Checks if the word is already in the array
			Finalnumbers.append(Finalwords.index(String[Wordschecked]))
			# Adds the number corresponding to the position in the words array to the numbers array
		else:
			Finalnumbers.append(Arrayword)
			# Adds the current word number to the numbers array
			Finalwords.append(String[Wordschecked])
			# Adds the current word to the words array
			Arrayword = Arrayword + 1
		Wordschecked = Wordschecked + 1
	Wordname = (input("What should the word file be called? ") + ".txt")
	Numbersname = (input("What should the numbers file be called? ") + ".txt")
	# Finds out what the user wants to call the files and adds ".txt" to the end
	Wordsfile = open(Wordname,'w')
	Numbersfile = open(Numbersname,'w')
	# Opens the named files
	Wordsfile = Wordsfile.write(str(Finalwords))
	Numbersfile = Numbersfile.write(str(Finalnumbers))
	# Writes to the files
	print ("Done!")
else:
	punctuation = "'[]"
	no_punctwords = ""
	no_punctnumbers = ""
	Currentword = 0
	Finalwords = ""
	# Create the variables
	Wordname = (input("What is the word file called? ") + ".txt")
	Numbersname = (input("What is the numbers file called? ") + ".txt")
	# Finds out what the user wants to called the file and adds ".txt" to the end
	Wordsfile = (open(Wordname,'r')).read()
	# Opens the named file
	for char in Wordsfile:
		if char not in punctuation:
			no_punctwords = no_punctwords + char
			# Removes any characters not required
	Numbersfile = (open(Numbersname,'r')).read()
	# Finds out what the user wants to called the file and adds ".txt" to the end
	for char in Numbersfile:
		if char not in punctuation:
			no_punctnumbers = no_punctnumbers + char
			# Removes any characters not required
	no_punctwords = no_punctwords.split(", ")
	no_punctnumbers = no_punctnumbers.split(", ")
	# Breaks the arrays back down into arrays
	no_punctnumbers = list(map(int, no_punctnumbers))
	# Converts the strings in the numbers array to integers
	for len in no_punctnumbers:
		Finalwords = (Finalwords + no_punctwords[no_punctnumbers[Currentword]] + " ")
		Currentword = Currentword + 1
		# Recreates the string by adding words corresponding to their position in the array
	print('Your string is "' + Finalwords + '"')
	Filewrite = input ("Do you want to write to a file? (Y/N) ").lower()
	if Filewrite == "y":
		Filename = (input("What should the file be called? ") + ".txt")
		# Finds out what the user wants to call the file and adds ".txt" to the end
		File = open(Filename,"w")
		# Opens the named files
		File = File.write(Finalwords)
		# Writes to the files
