winning = dict()
cards = 0

def processGame(game):
    sections = game.split(':')[1].strip().split('|')
    winningNums = set(sections[0].split())

    return len(winningNums.intersection(sections[1].split()))

with open('input') as inputFile:
    games = inputFile.read().split('\n')

    for i in range(len(games) - 1, -1, -1):
        game = games[i]
        wins = processGame(game)

        gameCards = wins
        for j in range(i + 1, i + 1 + wins):
            gameCards += winning[j]

        cards += gameCards + 1
        winning[i] = gameCards

    print(cards)
