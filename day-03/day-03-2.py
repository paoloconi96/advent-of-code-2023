from collections import defaultdict

gears = defaultdict(list)

def addGear(number, i, j):
    gears['{}.{}'.format(i, j)].append(number)

def searchGear(number, input, start, end, rowIndex, lineLength):
    if number == '':
        return
    number = int(number)

    if start > 0 and input[rowIndex][start - 1] == '*':
        addGear(number, rowIndex, start - 1)
    if end < lineLength - 1 and input[rowIndex][end + 1] == '*':
        addGear(number, rowIndex, end + 1)

    for i in range(start - 1, end + 2):
        if i < 0 or i > lineLength - 1:
            continue

        if rowIndex > 0 and input[rowIndex - 1][i] == '*':
            addGear(number, rowIndex - 1, i)

        if rowIndex < lineLength - 1 and input[rowIndex + 1][i] == '*':
            addGear(number, rowIndex + 1, i)

    return False

with open('input') as inputFile:
    output = 0
    input = inputFile.read().split('\n')
    lineLength = len(input[0])
    for rowIndex, line in enumerate(input):
        start = None
        number = ''
        for j, char in enumerate(line):
            if char.isdigit():
                if number == '':
                    start = j
                number += char
                continue

            searchGear(number, input, start, j - 1, rowIndex, lineLength)
            number = ''

        searchGear(number, input, start, j, rowIndex, lineLength)

    for numbers in gears.values():
        if len(numbers) == 2:
            output += numbers[0] * numbers[1]

    print(output)
