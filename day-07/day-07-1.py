from collections import defaultdict
from functools import cmp_to_key

def getHandTypeWeight(row):
    counts = defaultdict(int)

    for i in range(len(row)):
        counts[row[i]] += 1

    sortedCounts = sorted(counts.values(), reverse=True)
    match sortedCounts:
        case [5]:
            return 7
        case [4, 1]:
            return 6
        case [3, 2]:
            return 5
        case [3, 1, 1]:
            return 4
        case [2, 2, 1]:
            return 3
        case [2, 1, 1, 1]:
            return 2

    return 1

values = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
def comparator(p1, p2):
    if p1[0] != p2[0]:
        return p1[0] - p2[0]

    for i in range(len(p1[1])):
        diff = values.index(p1[1][i]) - values.index(p2[1][i])
        if diff != 0:
            return diff

    return 0

with open('input') as inputFile:
    rows = inputFile.readlines()
    pairValueMap = {}
    for row in rows:
        cards, value = row.split()
        pairValueMap[cards] = int(value)

    numberValueHands = []
    for row in pairValueMap.keys():
        numberValueHands.append((getHandTypeWeight(row), row))

    numberValueHands.sort(key=cmp_to_key(comparator))

    output = 0
    for i, hand in enumerate(numberValueHands):
        hand = hand[1]
        output += pairValueMap[hand] * (i + 1)

    print(output)
