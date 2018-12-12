array = []
while True:
    action = input("What action would you like to take? ").lower()
    if (action == "view"):
        print(array)
    elif (action == "add"):
        array.append(input("What would you like to add? "))
    elif (action == "remove"):
        if (array != []):
            array.pop()
