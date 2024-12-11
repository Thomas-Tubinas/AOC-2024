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
        else: 
            AdvChecker(changes, report)

advsafeReports = 0
def AdvChecker(changes, report):
    global advsafeReports
    global list
    for i in range(len(report)):
        isSafe = False
        advChanges = report.copy()
        advChanges.pop(i)
        reevaluation = [advChanges[i + 1] - advChanges[i] for i in range(len(advChanges) - 1)]
        for i in range(len(report)):
            if all(1 <= diff <= 3 for diff in reevaluation) or all(-3 <= diff <= -1 for diff in reevaluation):
                print("good")
                print(report)
                print(changes)
                print(advChanges)
                advsafeReports += 1
                isSafe = True
                break
        if(isSafe):
            break

Load()
Checker()
print(safeReports)
print(advsafeReports)