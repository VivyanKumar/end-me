list = ['Aditya','Rathiin', "Ihit", "Vivyan", 'Ram', 'Mohammed', 'Sunita', 'Aarav', 'Arnav', 'Ayaan']
lowerlist = []
upperlist = []
print("Options:")
print("(1) Enter an 11th name")
print("(2) Count the number of vowels in each name")
print("(3) If there is an incorrect name, replace it with an new one.")
print("(4) Find the middle characters")
print("(5) Convert all the names to Title Case. (Uppercase)")
print("(6) Calculate how many names start or end with 'a'")
print("(7) Exit")
x = int(input("Enter your choice: "))
if x == 1:
    print("Duplicate names will not be accepted.")
    y = input("Enter an 11th name:")
    for i in range(len(list)):
        lowerlist.append(list[i])
        lowerlist[i] = list[i].lower()
    if y in lowerlist:
        print("Duplicate values are not allowed")
    else:
        list.append(y)
        print(list)
elif x == 2:
    print("This will count the vowels in each name.")
    for i in range(len(list)):
        lowerlist.append(list[i])
        lowerlist[i] = list[i].lower()
        count = lowerlist[i].count('a') + lowerlist[i].count('e') + lowerlist[i].count('i') + lowerlist[i].count('o') + lowerlist[i].count('u')
        print("The number of vowels in", list[i], "is", count)
elif x == 3:
    print(list)
    Name = input("Enter the name you want to replace: ")
    ReplacedName = input("Enter the replacement name: ")
    for i in range(len(list)):
        lowerlist.append(list[i])
        lowerlist[i] = list[i].lower()
        if Name.lower() == lowerlist[i]:
            Name = (Name[0].upper() + Name[1:])
            list.remove(Name)
            list.insert(i, ReplacedName)
            print(list)
            break
    else:
        print("The name is not in the list.")
elif x == 4:
    for i in range(len(list)):
        if len(list[i]) == 4:
            print("The middle characters of", list[i], "are:", list[i][1:-1])
        elif len(list[i]) == 3:
            print("The middle characters of", list[i], "are:", list[i][1:-1])
        elif len(list[i]) % 2 == 0 and len(list[i]) != 3 and len(list[i]) != 4:
            print("The middle characters of", list[i], "are:", list[i][((len(list[i]) - 1) // 2):(((len(list[i]) - 1) // 2) * 2)])
        else:
            print("The middle characters of", list[i], "are:", list[i][(len(list[i]) // 2 - 1) :(len(list[i]) // 2 + 2) ] )
elif x == 5:
    for i in range(len(list)):
        upperlist.append(list[i])
        upperlist[i] = list[i].upper()
    print(upperlist)
elif x == 6:
    for i in range(len(list)):
        lowerlist.append(list[i])
        lowerlist[i] = list[i].lower()
        if lowerlist[i][0:1] == 'a' or lowerlist[i][len(list[i])-1] == 'a':
            print(list[i], "starts or ends with 'a'.")
        else:
            print(list[i], "does not start or end with 'a'.")
elif x == 7:
    print("Thanks for using this program!")
else:
    print("The number must be between 1 and 7")
