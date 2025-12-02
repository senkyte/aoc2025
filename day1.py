with open("adventofcode2025/day1input.txt","r") as input_text:
    position = 50 # Starting position
    count0 = 0 # counter
    line = input_text.readline()
    while(line != ""):
        line = line.strip()
        rotation = int(line[1:])
        if line[0] == 'L':
             position -= rotation
             while position < 0:
                 position += 100
                 count0 += 1
    
        else:
            position += rotation
            while position > 99:
                position -= 100
                count0 += 1

        line = input_text.readline()
    print(count0)