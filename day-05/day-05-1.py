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
                'sourceEnd': int(row[1]) + int(row[2]),
                'offset': int(row[0]) - int(row[1]),
            })

        maps.sort(key=lambda x: x['sourceStart'])
        mapsList.append(maps)

    seeds = data[0].split()
    output = 2 ** 32
    for i in range(1, len(seeds)):
        seed = int(seeds[i])
        for map in mapsList:
            index = bisect_left(map, seed, key=lambda x: x['sourceEnd'])
            if index < len(map) and map[index]['sourceStart'] <= seed:
                seed = seed + map[index]['offset']
        output = min(output, seed)

    print(output)
