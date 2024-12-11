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
    for item1, item2 in zip(list1, list2):
        char1 = str(item1)
        char2 = str(item2)
        result = abs(int(char1) - int(char2))
        print(result)
        finalDistance = int(result) + int(finalDistance)
    print(finalDistance)

Load()
Dicer()