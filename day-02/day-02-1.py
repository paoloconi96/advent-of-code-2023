def parseGame(input):
    gameRounds = input.split(';')
    for i, round in enumerate(gameRounds):
        roundArray = round.split()
        j = 0
        if i == 0:
            id = int(roundArray[1][:-1])
            j = 2

        while j < len(roundArray):
            print(roundArray, j)
            if roundArray[j+1] == 'red' and int(roundArray[j]) > 12:
                return None
            if roundArray[j+1] == 'green' and int(roundArray[j]) > 13:
                return None
            if roundArray[j+1] == 'blue' and int(roundArray[j]) > 14:
                return None

            j += 2

    return id

with open('input', 'r') as inputFile:
    output = 0
    for line in inputFile:
        result = parseGame(line.strip().replace(',', ''))
        output += result if result is not None else 0

    print(output)
