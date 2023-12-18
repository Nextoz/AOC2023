data = open('Input18.txt', 'r').read().strip().split('\n')
dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

# Part 1
x, y, borders = 0, 0, []
for row in data:
    d, m, _ = row.split()
    dx, dy = move[d]
    for _ in range(int(m) ):
        borders.append( (x, y) )
        x, y = x + dx, y + dy

# Shoelace formula
area = 0
for i in range(len(borders) - 1):
    x1, y1 = borders[i]
    x2, y2 = borders[i + 1]
    area += x1 * y2 - x2 * y1

# Pick's theorem
perimeter = len(borders)
interior_area = abs(area) // 2 - perimeter // 2 + 1
print('Part 1:', interior_area + perimeter)


x, y, borders = 0, 0, []
for row in data:
    _, _, c = row.split()
    c = c[1:-1]
    d, m = dirs[c[-1]], int(c[1:-1], 16) 
    dx, dy = move[d]
    for _ in range(int(m) ):
        borders.append( (x, y) )
        x, y = x + dx, y + dy

# Shoelace formula
area = 0
for i in range(len(borders) - 1):
    x1, y1 = borders[i]
    x2, y2 = borders[i + 1]
    area += x1 * y2 - x2 * y1

# Pick's theorem
perimeter = len(borders)
interior_area = abs(area) // 2 - perimeter // 2 + 1
print('Part 2:', interior_area + perimeter)