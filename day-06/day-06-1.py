import math

def checkTime(time, minDistance, t):
    running = time - t
    runDistance = t * running
    return int(runDistance > minDistance)

with open('input') as inputFile:
    data = inputFile.read().split('\n')
    times = data[0].split()[1:]
    distances = data[1].split()[1:]

    races = []
    for i in range(len(times)):
        races.append({
            'time': int(times[i].strip()),
            'distance': int(distances[i].strip())
        })

    output = 1
    for race in races:
        minDistance = race['distance']
        time = race['time']
        valid = checkTime(time, minDistance, time // 2) if time % 2 == 0 else 0
        for t in range(1, math.ceil(time / 2)):
            valid += checkTime(time, minDistance, t) * 2
        output *= valid

    print(output)
