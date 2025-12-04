with open("day4input.txt","r") as map:
    # cleaning
    f = map.readlines()
    rows = [list(line.strip()) for line in f]

    width = len(rows[0])
    height = len(rows)
    # checking validity of every roll
    total = 0
    valid = 0
    while True:
        for y in range(height):
            for x in range(width):
                if rows[y][x] == "@":
                    counter = 0
                    for i in range(y - 1, y + 2):
                        for j in range(x - 1, x + 2):
                            if i == y and j == x:
                                continue
                            if 0 <= i < height and 0 <= j < width:
                                if rows[i][j] == "@":
                                    counter += 1
                                if counter >= 4:
                                    break
                    if counter < 4:
                        valid += 1
                        rows[y][x] = ""

                else:
                    continue 
        if valid == 0:
            break
        else:
            total += valid
            valid = 0

    
    print(total)