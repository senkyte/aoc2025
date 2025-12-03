# read the file
with open("day2input.txt","r") as data:
    ranges = data.readline().split(",")
    total = 0
    for i in ranges:
        id = i.split("-")
        for j in range(int(id[0]),int(id[1])+1):
            string = str(j)
            if string in (string + string)[1:-1]:
                total += j
    print(total)