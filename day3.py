def largest_number(bank, k):
    stack = []
    remove = len(bank) - k

    for digit in bank:
        while stack and remove > 0 and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)

    return int("".join(stack[:k]))



with open("day3input.txt", "r") as data:
    largest = []
    position1 = 0
    bank = data.readline().strip()
    total = 0
    while(bank != ""):
        total += largest_number(bank,12)
        bank = data.readline().strip()
    print(total)