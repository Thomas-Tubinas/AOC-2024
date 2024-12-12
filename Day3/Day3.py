import re

list = []

def Load():
    with open ("day3log.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            list.append(line)

def FilterList(list):
    filteringList = []
    def checkChar(char):
        vaildChar = ['m', 'u', 'l', '(', ')' , ',',]
        for i in vaildChar:
            if(char == i):
                return char
            elif(char.isdigit()):
                return char

    
    for strings in list:
        filteredString = ''.join(filter(checkChar, strings))
        filteringList.append(filteredString)

    return filteringList

Load()
filteredList = FilterList(list)
print(filteredList)