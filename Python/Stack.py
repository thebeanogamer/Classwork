array = []
proceed = True
while proceed:
    action = input("What action would you like to take? ").lower()
    if (action == "view"):
        print(array)
    elif (action == "add"):
        array.append(input("What would you like to add? "))
    elif (action == "remove"):
        if (array != []):
            array.pop()
    elif (action == "exit"):
        proceed = False
    else:
        print("Unrecognised Command")
