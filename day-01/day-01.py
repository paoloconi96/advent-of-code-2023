digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def computeDigit(input):
    if input[0].isnumeric():
        return int(input[0])

    for i, digit in enumerate(digits):
        if input[:len(digit)] == digit:
            return i + 1

    return None

def computeNumber(input):
    first = None
    last = None

    for i in range(len(input)):
        if first != None and last != None:
            break

        if first == None:
            first = computeDigit(input[i:])
        if last == None:
            last = computeDigit(input[-i-1:])

    return first * 10 + last

with open('input', 'r') as inputFile:
    output = 0
    for line in inputFile:
        output += computeNumber(line.strip())

    print(output)
