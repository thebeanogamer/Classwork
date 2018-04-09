Names = ["Fred","Sue","Daniel","James","Alex","Josh","Robert"]
a = 0
age = 0
while a < len(Names):
	print ("Hello", Names[a])
	age = int(input("How old are you? "))
	if age <= 16:
		print ("You should still be at school!")
	else:
		print ('You are a "responsible" adult!')
	a = a + 1
