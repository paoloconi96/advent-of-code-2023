with open('input') as inputFile:
    rows = inputFile.read().split('\n')
    directions = rows[0]

    treeMap = {}
    nextNode = 'AAA'
    for steps in range(2, len(rows)):
        row = rows[steps]
        treeMap[row[:3]] = (row[7:10], row[12:15])

    steps = 0
    while nextNode != 'ZZZ':
        directionIndex = steps % len(directions)
        direction = 0 if directions[directionIndex] == 'L' else 1
        nextNode = treeMap[nextNode][direction]
        steps += 1

    print(steps)
