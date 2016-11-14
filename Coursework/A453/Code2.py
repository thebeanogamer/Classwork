punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~£'''
no_punct1 = ""
wordschecked = 0
# the position in the users input
wordchecklooppos = 0
# the position in the words array
wordcheckstring = 0
finalwords = [None]
finalnumbers = [None]
alreadydone = False

String = str(input("What is your string? ").lower())
while String == "":
	print("Umm, no. I need something to work with!")
	String = input("What is your string? ").lower()
for char in String:
	if char not in punctuation:
		no_punct1 = no_punct1 + char
no_punct1 = no_punct1.split()
while wordschecked != len(no_punct1):
	while wordchecklooppos != len(finalwords):
		if finalwords[wordchecklooppos] == no_punct1[wordschecked]:
			alreadydone = True
	if alreadydone == False:
		finalwords = finalwords.append(no_punct1[wordschecked])
		finalnumbers = finalnumbers.append(wordchecklooppos)
		wordchecklooppos = wordchecklooppos + 1
	else:
		finalnumbers = finalnumbers.append(wordschecked)
		wordchecklooppos = wordchecklooppos + 1
	alreadydone = False
	wordschecked = wordschecked + 1
print (finalwords)
print (finalnumbers)
