Realcommand = False
Command = input("Do you want to encrypt or decrypt? ").lower()
while Realcommand == False:
	if Command == "":
		print ("Um, no. Give me somethingto work with!")
		Command = input("Do you want to encrypt or decrypt? ").lower()
	elif Command == "encrypt" or Command == "decrypt":
		Realcommand = True
	else:
		print ("Um, no. Give me something I understand!")
		Command = input("Do you want to encrypt or decrypt? ").lower()
if Command == "encrypt":
	Wordschecked = 0
	Finalwords = []
	Finalnumbers = []
	Arrayword = 0
	String = input("What is your string? ")
	String = String.split()
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
	Wordsfile = open(Wordname,'w')
	Numbersfile = open(Numbersname,'w')
	Wordsfile = Wordsfile.write(str(Finalwords))
	Numbersfile = Numbersfile.write(str(Finalnumbers))
	print ("Done!")
else:
	punctuation = "'[]"
	no_punctwords = ""
	no_punctnumbers = ""
	Currentword = 0
	Finalwords = ""
	Wordname = (input("What is the word file called? ") + ".txt")
	Numbersname = (input("What is the numbers file called? ") + ".txt")
	Wordsfile = (open(Wordname,'r')).read()
	for char in Wordsfile:
		if char not in punctuation:
			no_punctwords = no_punctwords + char
	Numbersfile = (open(Numbersname,'r')).read()
	for char in Numbersfile:
		if char not in punctuation:
			no_punctnumbers = no_punctnumbers + char
	no_punctwords = no_punctwords.split(", ")
	no_punctnumbers = no_punctnumbers.split(", ")
	no_punctnumbers = list(map(int, no_punctnumbers))
	for len in no_punctnumbers:
		Finalwords = (Finalwords + no_punctwords[no_punctnumbers[Currentword]] + " ")
		Currentword = Currentword + 1
	print("Your string is", Finalwords)
	Filewrite = input ("Do you want to write to a file? (Y/N) ").lower()
	if Filewrite == "y":
		Filename = (input("What should the file be called? ") + ".txt")
		File = open(Filename,"w")
		File = File.write(Finalwords)
