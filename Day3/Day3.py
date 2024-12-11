list = []

def Load():
    substring = "mul("
    with open ("log.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if substring in line:
                list.append(line)


Load()
print(list)