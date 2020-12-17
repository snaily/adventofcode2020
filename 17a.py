import sys

initial = []
with open(sys.argv[1]) as file:
    for line in file:
        initial.append(list(line.strip()))

universe = [[['.' for x in range(len(initial[0]) + 12)] for y in range(len(initial) + 12)] for z in range(1 + 12)]

for x in range(len(initial[0])):
    for y in range(len(initial)):
        universe[6][y+6][x+6] = initial[y][x]

def print_universe(universe):
    print('\n\n'.join('\n'.join(''.join(line) for line in field) for field in universe))

def generation(universe):
    universe_next = [[['.' for x in range(len(initial[0]) + 12)] for y in range(len(initial) + 12)] for z in range(1 + 12)]
    for z, field in enumerate(universe):
        for y, line in enumerate(field):
            for x, _ in enumerate(line):
                neighbors = 0
                for dz in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if dz == 0 and dy == 0 and dx == 0:
                                continue
                            if not (0 <= x+dx < len(line)) or not (0 <= y+dy < len(field)) or not (0 <= z+dz < len(universe)):
                                continue
                            if universe[z+dz][y+dy][x+dx] == '#':
                                neighbors += 1
                if universe[z][y][x] == '.' and neighbors == 3:
                    universe_next[z][y][x] = '#'
                elif universe[z][y][x] == '#' and (neighbors < 2 or neighbors > 3):
                    universe_next[z][y][x] = '.'
                else:
                    universe_next[z][y][x] = universe[z][y][x]
    return universe_next

for i in range(6):
    universe = generation(universe)

print(sum(sum(line.count('#') for line in field) for field in universe))
