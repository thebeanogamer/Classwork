punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~£'''
StringPos = 0
ArrayPos = 0
Happens = False
Finalstring = ""
Finalnumbers = ""

String = str(input("What is your string? ").lower())
while String == "":
	print("Umm, no. I need something to work with!")
	String = input("What is your string? ").lower()
for char in String:
	if char not in punctuation:
		Finalstring = Finalstring + char
Finalstring = str(Finalstring.split())
while StringPos != len(Finalstring):
	while ArrayPos != len(String):
		if Finalstring[ArrayPos] == Finalstring [ArrayPos]:
			Happens = True
			break
		ArrayPos = ArrayPos + 1
	if Happens == True:
		Finalnumbers = Finalnumbers + str(ArrayPos)
	else:
		FinalWords = Finalwords.append(String[StringPos])
		Finalnumbers = Finalnumber.append(ArrayPos + 1)
	StringPos = StringPos + 1
print(Finalnumbers)
print(FinalWords)
#Open files to replace
#Write FinalWords to file
#Write Finalnumbers to file
