import os

Punctuation = ["!",'"',"£","$","%","^","&","*","(",")","-","=","_","+","{""}",":","[","]",";","@","'","~","#","<",">",",",".","?","/","¬","`","/","*","-","+"]

def RemovePunctuation(Original):
	y = 0
	z = 0
	Words = len(Original)
	while y != Words:
		while z != len(Punctuation):
			Original[x].replace(Punctuation[y],"")
			z = z + 1
		y = y + 1
		z = 0
	y = y + 1

Continue = True
while Continue == True:
	x = 0
	a = 0
	String = input("What is the string: ").lower().split()
	while a != len(String):#
		
	Term = input("What is the search term: ").lower().split()
	while x != len(String):
		if Term == String[x]:
			print("Word", (x + 1))
		x = x + 1
	ContinueRaw = input("Continue Y/N ").lower()
	if ContinueRaw == "n":
		Continue = False
	else:
		os.system('cls')
