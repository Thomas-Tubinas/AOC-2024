list1 = []
list2 = []

def Load():
    with open ("list.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            list1.append(line)

    with open ("list2.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            list2.append(line)

finalDistance = 0
def Dicer():
    global finalDistance
    for item in list1:
        counter = 0
        char = str(item)
        for items in list2:
            if(char == str(items)):
                counter = counter + 1
        result = counter * int(char)
        finalDistance += result
    print(finalDistance)

Load()
Dicer()