import random
x = 0
Names = ["Ulli","Dwight","Brady","Waldo","Florus","Sullivan","Ramsey","Howard","Laurent","Raimund","Amira","Felicia","Cassandra","Selma","Zaria","Sorren","Voletta","Rieke","Sibilla","Liane"]
while x != 2:
	NamePos = random.randint(0,19)
	Number1 = random.randint(1,12)
	Number2 = random.randint(1,4)
	Number3 = random.randint(1,12)
	Number4 = random.randint(1,4)
	FinalNumber1 = 10 + int(Number1 / Number2)
	FinalNumber2 = 10 + int(Number3 / Number4)
	YourName = (Names[NamePos])
	file = open("File.txt",'a')
	file.write(str(FinalNumber1) + " " + str(FinalNumber2) + " " + YourName)
	file.write('\n')
	file.close()
	x = x + 1
