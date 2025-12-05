with open("day5input.txt", "r") as data:
    range2 = []
    valid = 0
    line = data.readline()
    while("-" in line):
        ranges = line.strip().split("-")
        lower = int(ranges[0])
        upper = int(ranges[1])
        range2.append([lower,upper])
        line = data.readline()
    line = data.readline()
    while(line != ""):
        isValid = False
        for i in range(len(range2)):
            if range2[i][0] < int(line) < range2[i][1]:
                isValid = True
        if isValid == True:
            valid += 1
        line = data.readline()
        print("still running...")
    print(valid) 