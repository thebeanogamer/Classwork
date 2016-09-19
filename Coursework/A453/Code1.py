import os

Continue = True
while Continue == True:
	x = 0
	String = input("What is the string: ").lower()
	String = String.split()
	Term = input("What is the search term: ").lower()
	while x < (len(String)):
		if Term == String[x]:
			print("Pos", (x + 1))
		x = x + 1
	ContinueRaw = input("Continue Y/N ").lower()
	if ContinueRaw == "n":
		Continue = False
	else:
		os.system('cls')
