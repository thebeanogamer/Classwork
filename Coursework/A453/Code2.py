punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~£'''
no_punct1 = ""
wordschecked = 0
finalwords = []
finalnumbers = []

String = str(input("What is your string? ").lower())
while String == "":
	print("Umm, no. I need something to work with!")
	String = input("What is your string? ").lower()
for char in String:
	if char not in punctuation:
		no_punct1 = no_punct1 + char
no_punct1 = no_punct1.split()
while wordschecked != len(no_punct1):
	if any(no_punct1[wordschecked] in s for s in finalwords):
		finalnumbers.append(finalwords.index(no_punct1[wordschecked]))
	else:
		finalnumbers.append(wordschecked)
		finalwords.append(no_punct1[wordschecked])
	wordschecked = wordschecked + 1
print (finalwords)
print (finalnumbers)
wordsfile = open("words.txt",'w')
numbersfile = open("numbers.txt", 'w')
wordsfile = wordsfile.write(str(finalwords))
numbersfile = numbersfile.write(str(finalnumbers))
