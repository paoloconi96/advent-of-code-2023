with open('input') as inputFile:
    points = 0
    games = inputFile.read().split('\n')

    for game in games:
        nums = game.split(':')[1].strip()
        sections = nums.split('|')

        winning = set(sections[0].split())

        match = len(winning.intersection(sections[1].split()))
        points += 2 ** (match - 1) if match > 0 else 0

    print(points)
