symbols = {'+', '-', '*', '#', '$', '&', '@', '/', '=', '%'}

def searchSymbol(number, input, start, end, rowIndex, lineLength):
    if number == '':
        return 0

    number = int(number)

    if start > 0 and input[rowIndex][start - 1] in symbols:
        return number
    if end < lineLength - 1 and input[rowIndex][end + 1] in symbols:
        return number

    for i in range(start - 1, end + 2):
        if i < 0 or i > lineLength - 1:
            continue

        if rowIndex > 0 and input[rowIndex - 1][i] in symbols:
            return number

        if rowIndex < lineLength - 1 and input[rowIndex + 1][i] in symbols:
            return number

    return 0

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

            output += searchSymbol(number, input, start, j - 1, rowIndex, lineLength)
            number = ''

        output += searchSymbol(number, input, start, j, rowIndex, lineLength)

    print(output)
