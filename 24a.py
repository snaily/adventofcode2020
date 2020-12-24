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

print(len(black))