list1 = []
list2 = []

def Load():
    open with ("sortedList1.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            list1.appead(line)

    open with ("sortedList2.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            list2.appead(line)

finalDistance = 0
def Dicer():
    global finalDistance
    for item1, item2 in zip(list1, list2):
        for i in range(5):
            char1 = str(item1)[i]
            char2 = str(item2)[i]
            result = int(char1) + int(char2)
            print(result)
            finalDistance = int(result) + int(finalDistance)
    print(finalDistance)

Load()
Dicer()