import os

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

Continue = True
while Continue == True:
	x = 0
	a = 0
	String = input("What is the string: ").lower()
	no_punct1 = ""
	for char in String:
		if char not in punctuations:
			no_punct1 = no_punct1 + char
	no_punct1 = no_punct1.split()
	Term = input("What is the search term: ").lower()
	while x != len(no_punct1):
		if Term == no_punct1[x]:
			print("Word", (x + 1))
		x = x + 1
	ContinueRaw = input("Continue Y/N ").lower()
	if ContinueRaw == "n":
		Continue = False
	else:
		os.system('cls')
