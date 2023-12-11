with open('input') as inputFile:
    initialUniverse = inputFile.read().split('\n')
    universe = []
    galaxyLocations = []
    noGalaxyRows = []
    noGalaxyColumns = []

    for i, row in enumerate(initialUniverse):
        universe.append(list(row))
        if row == '.' * len(initialUniverse[0]):
            noGalaxyRows.append(i)

    for i in range(len(universe[0])):
        noGalaxy = True
        for row in universe:
            if row[i] != '.':
                noGalaxy = False
                break

        if noGalaxy:
            noGalaxyColumns.append(i)

    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == '#':
                galaxyLocations.append((i, j))

    output = 0
    for i, location in enumerate(galaxyLocations):
        for j, location2 in enumerate(galaxyLocations[i+1:]):
            x = range(min(location[1], location2[1]), max(location[1], location2[1]))
            y = range(min(location[0], location2[0]), max(location[0], location2[0]))
            diffx = y.stop - y.start
            diffy = x.stop - x.start

            for k in noGalaxyRows:
                if k in y:
                    diffy += 1
                elif k > y.start:
                    break

            for k in noGalaxyColumns:
                if k in x:
                    diffx += 1
                elif k > x.start:
                    break

            output += diffy + diffx

    print(output)
