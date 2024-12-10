list = []

def Load():
    with open ("log.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            list.append([int(x) for x in line.split()])

safeReports = 0
def Checker():
    global safeReports
    global list
    for report in list:
        changes = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        if all(1 <= diff <= 3 for diff in changes) or all(-3 <= diff <= -1 for diff in changes):
            safeReports += 1

Load()
Checker()
print(safeReports)