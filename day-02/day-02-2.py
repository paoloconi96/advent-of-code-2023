def parseGame(input):
    gameRounds = input.split(';')
    red = 0
    green = 0
    blue = 0

    for i, round in enumerate(gameRounds):
        roundArray = round.split()
        j = 0
        if i == 0:
            j = 2

        while j < len(roundArray):
            number = int(roundArray[j])
            if roundArray[j+1] == 'red' and number > red:
                red = number
            elif roundArray[j+1] == 'green' and number > green:
                green = number
            elif roundArray[j+1] == 'blue' and number > blue:
                blue = number

            j += 2

    return red * green * blue

with open('input', 'r') as inputFile:
    output = 0
    for line in inputFile:
        output += parseGame(line.strip().replace(',', ''))

    print(output)
