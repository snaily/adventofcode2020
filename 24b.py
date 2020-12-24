import sys

dirs = {
    'ne': (1,-1),
    'e': (2,0),
    'se': (1,1),
    'nw': (-1,-1),
    'w': (-2,0),
    'sw': (-1,1),
}

black = set()
with open(sys.argv[1]) as file:
    for line in file:
        line=line.strip()
        pos = (0, 0)
        while line:
            dir, line = line[0], line[1:]
            if dir in ('s','n'):
                dir, line = dir+line[0], line[1:]
            pos = tuple(p+d for p, d in zip(pos, dirs[dir]))
        if pos in black:
            black.remove(pos)
        else:
            black.add(pos)

def evolve(black):
    neighbors = {tile: 0 for tile in black}
    for tile in black:
        for dir in dirs.values():
            pos = tuple(t+d for t, d in zip(tile, dir))
            n = neighbors.get(pos, 0) + 1
            neighbors[pos] = n
    new_black = set()
    for tile in neighbors.keys():
        if tile in black and (neighbors[tile] == 1 or neighbors[tile] == 2):
            new_black.add(tile)
        elif neighbors[tile] == 2: # white
            new_black.add(tile)
    return new_black

for i in range(100):
    black = evolve(black)
    print(i+1, len(black))
