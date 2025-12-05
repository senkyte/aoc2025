with open("day5input.txt", "r") as data:
    ranges = []
    for line in data:
        if "-" not in line:
            break
        lower, upper = map(int, line.strip().split("-"))
        ranges.append([lower, upper])
    
    ranges.sort()
    
    merged = []
    current = ranges[0]
    for r in ranges[1:]:
        if r[0] <= current[1] + 1:
            current[1] = max(r[1],current[1])
        else:
            merged.append(current)
            current = r
    merged.append(current)
    valid = 0
    for i in range(len(merged)):
        valid = valid + merged[i][1] - merged[i][0] + 1
    print(valid)