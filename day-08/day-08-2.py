import math

with open('input') as inputFile:
    rows = inputFile.read().split('\n')
    directions = rows[0]

    treeMap = {}
    nextNodes = []
    for steps in range(2, len(rows)):
        row = rows[steps]
        node = row[:3]

        treeMap[node] = (row[7:10], row[12:15])
        if node[2] == 'A':
            nextNodes.append(node)

    steps = 0
    winners = []
    for nextNode in nextNodes:
        while nextNode[2] != 'Z':
            directionIndex = steps % len(directions)
            direction = 0 if directions[directionIndex] == 'L' else 1
            nextNode = treeMap[nextNode][direction]
            steps += 1

        winners.append(steps)
        steps = 0

    print(math.lcm(*winners))
