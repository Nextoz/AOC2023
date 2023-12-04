import sys


lines = open(sys.argv[1], 'r').readlines()

def part1():
    total = 0
    for line in lines:
        x, y = map(str.split, line.split('|'))
        matches = set(x) & set(y)
        total += 2 ** (len(matches) - 1) if matches else 0
    return total

def part2():
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        x, y = map(str.split, line.split('|'))
        n = len(set(x) & set(y))
        for j in range(i + 1, min(i + 1 + n, len(lines))):
            cards[j] += cards[i]
    return sum(cards)

print(part1(), part2())