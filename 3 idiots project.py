lst = ['Aditya','Rathiin', "Ihit", "Vivyan", 'Ram', 'Mohammed', 'Sunita', 'Aarav', 'Arnav', 'Ayaan']
lowerlist = []
upperlist = []

print("Options:")
print("(0) Exit")
print("(1) Enter an 11th name")
print("(2) Count the number of vowels in each name")
print("(3) If there is an incorrect name, replace it with an new one.")
print("(4) Find the middle characters")
print("(5) Convert all the names to Title Case. (Uppercase)")
print("(6) Calculate how many names start or end with 'a'")

def function1():
    print("Duplicate names will not be accepted.")
    errorCount = 0
    while errorCount < 3:
        y = input("Enter an 11th name: ")
        for i in range(len(lst)):
            lowerlist.append(lst[i])
            lowerlist[i] = lst[i].lower()
        if y in lowerlist:
            print("Duplicate values are not allowed")
            errorCount+=1
        else:
            lst.append(y)
            print(lst)
            break
def function2():
    print("This will count the vowels in each name.")
    for i in range(len(lst)):
        lowerlist.append(lst[i])
        lowerlist[i] = lst[i].lower()
        count = lowerlist[i].count('a') + lowerlist[i].count('e') + lowerlist[i].count('i') + lowerlist[i].count('o') + \
                lowerlist[i].count('u')
        print("The number of vowels in", lst[i], "is", count)
def function3():
    print(lst)
    Name = input("Enter the name you want to replace: ")
    ReplacedName = input("Enter the replacement name: ")
    for i in range(len(lst)):
        lowerlist.append(lst[i])
        lowerlist[i] = lst[i].lower()
        if Name.lower() == lowerlist[i]:
            Name = (Name[0].upper() + Name[1:])
            lst.remove(Name)
            lst.insert(i, ReplacedName)
            print(lst)
            break
    else:
        print("The name is not in the list.")
def function4():
    for i in range(len(lst)):
        if len(lst[i]) == 4:
            print("The middle characters of", lst[i], "are:", lst[i][1:-1])
        elif len(lst[i]) == 3:
            print("The middle characters of", lst[i], "are:", lst[i][1:-1])
        elif len(lst[i]) % 2 == 0 and len(lst[i]) != 3 and len(lst[i]) != 4:
            print("The middle characters of", lst[i], "are:",
                  lst[i][((len(lst[i]) - 1) // 2):(((len(lst[i]) - 1) // 2) * 2)])
        else:
            print("The middle characters of", lst[i], "are:", lst[i][(len(lst[i]) // 2 - 1):(len(lst[i]) // 2 + 2)])
def function5():
    for i in range(len(lst)):
        upperlist.append(lst[i])
        upperlist[i] = lst[i].capitalize()
    print(upperlist)
def function6():
    for i in range(len(lst)):
        lowerlist.append(lst[i])
        lowerlist[i] = lst[i].lower()
        if lowerlist[i][0:1] == 'a' or lowerlist[i][len(lst[i]) - 1] == 'a':
            print(lst[i], "starts or ends with 'a'.")
        else:
            print(lst[i], "does not start or end with 'a'.")

functions = [function1, function2, function3, function4, function5, function6]

while True:
    x = int(input("Enter your choice: "))
    if x in range(1, 6):
        functions[x-1]()
    elif x == 0:
        print("now exiting the program")
        break
    else:
        print("Invalid input")
