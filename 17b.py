import sys

initial = []
with open(sys.argv[1]) as file:
    for line in file:
        initial.append(list(line.strip()))

multiverse = [[[['.' for x in range(len(initial[0]) + 12)] for y in range(len(initial) + 12)] for z in range(1 + 12)] for w in range(1 + 12)]

for x in range(len(initial[0])):
    for y in range(len(initial)):
        multiverse[6][6][y+6][x+6] = initial[y][x]

def print_multiverse(multiverse):
    print('\n\n'.join('\n|\n'.join('\n'.join(''.join(line) for line in field) for field in universe) for universe in multiverse))

def generation(multiverse):
    multiverse_next = [[[['.' for x in range(len(initial[0]) + 12)] for y in range(len(initial) + 12)] for z in range(1 + 12)] for w in range(1 + 12)]
    for w, universe in enumerate(multiverse):
        for z, field in enumerate(universe):
            for y, line in enumerate(field):
                for x, _ in enumerate(line):
                    neighbors = 0
                    for dw in [-1, 0, 1]:
                        for dz in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                for dx in [-1, 0, 1]:
                                    if dw==0 and dz == 0 and dy == 0 and dx == 0:
                                        continue
                                    if not (0 <= x+dx < len(line)) or not (0 <= y+dy < len(field)) or not (0 <= z+dz < len(universe)) or not (0 <= w+dw < len(multiverse)):
                                        continue
                                    if multiverse[w+dw][z+dz][y+dy][x+dx] == '#':
                                        neighbors += 1
                    if multiverse[w][z][y][x] == '.' and neighbors == 3:
                        multiverse_next[w][z][y][x] = '#'
                    elif multiverse[w][z][y][x] == '#' and (neighbors < 2 or neighbors > 3):
                        multiverse_next[w][z][y][x] = '.'
                    else:
                        multiverse_next[w][z][y][x] = multiverse[w][z][y][x]
    return multiverse_next

for i in range(6):
    print(f'gen {i}')
    multiverse = generation(multiverse)

print(sum(sum(sum(line.count('#') for line in field) for field in universe) for universe in multiverse))
