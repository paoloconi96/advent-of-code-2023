with open('input') as inputFile:
    histories = inputFile.read().split('\n')

    for k in range(len(histories)):
        history = histories[k]
        valuesList = [list(int(i) for i in history.split())]

        i = 0
        while i < len(valuesList):
            values = valuesList[i]
            newValues = []
            stop = True
            for j in range(1, len(valuesList[i])):
                diff = values[j] - values[j - 1]
                if diff != 0:
                    stop = False
                newValues.append(diff)

            valuesList.append(newValues)
            if stop:
                break
            i += 1

        histories[k] = valuesList

    output = 0
    for history in histories:
        history[-1].append(0)

        for i in range(len(history) - 1, 0, -1):
            history[i - 1].append(history[i][-1] + history[i - 1][-1])

        output += history[0][-1]

    print(output)