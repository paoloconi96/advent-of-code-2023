import math

def checkTime(time, minDistance, t):
    running = time - t
    runDistance = t * running
    return int(runDistance > minDistance)

with open('input') as inputFile:
    data = inputFile.read().split('\n')
    time = int(data[0][10:].replace(' ', ''))
    minDistance = int(data[1][10:].replace(' ', ''))

    output = checkTime(time, minDistance, time // 2) if time % 2 == 0 else 0
    for t in range(1, math.ceil(time / 2)):
        output += checkTime(time, minDistance, t) * 2

    print(output)
