from bisect import bisect_left

with open('input') as inputFile:
    data = inputFile.read().split('\n\n')

    mapsList = []
    for i in range(1, len(data)):
        mapData = data[i].split('\n')
        maps = []
        for j in range(1, len(mapData)):
            row = mapData[j].split()
            maps.append({
                'sourceStart': int(row[1]),
                'sourceEnd': int(row[1]) + int(row[2]) - 1,
                'offset': int(row[0]) - int(row[1]),
            })

        maps.sort(key=lambda x: x['sourceStart'])
        mapsList.append(maps)

    seeds = data[0].split()
    seedRanges = []
    for i in range(1, len(seeds) - 1, 2):
        seedRanges.append((int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])))

    output = 2 ** 32
    for map in mapsList:
        newSeedRanges = []
        i = 0
        while i < len(seedRanges):
            rangeStart = seedRanges[i][0]
            rangeEnd = seedRanges[i][1]

            index = bisect_left(map, rangeStart, key=lambda x: x['sourceEnd'])
            if index >= len(map):
                newSeedRanges.append(seedRanges[i])
                i += 1
                continue

            if rangeStart < map[index]['sourceStart']:
                newSeedRanges.append((rangeStart, map[index]['sourceStart'] - 1))

            newSeedRanges.append((
                max(map[index]['sourceStart'], rangeStart) + map[index]['offset'],
                min(rangeEnd, map[index]['sourceEnd']) + map[index]['offset']),
            )

            if rangeEnd > map[index]['sourceEnd']:
                seedRanges.append((map[index]['sourceEnd'] + 1, rangeEnd))

            i += 1

        seedRanges = newSeedRanges

    output = seedRanges[0][0]
    for range in seedRanges:
        if range[0] != 0:
            output = min(output, range[0])

    print(output)
