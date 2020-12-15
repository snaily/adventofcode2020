import sys

DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
pos = (0, 0)
dir = DIRS[0]

def forward(pos, dir, amount):
    pos = (pos[0] + amount*dir[0], pos[1] + amount*dir[1])
    return pos, dir
def left(pos, dir, amount):
    index = DIRS.index(dir)
    dir = DIRS[(index - (amount//90)) % 4]
    return pos, dir
def right(pos, dir, amount):
    index = DIRS.index(dir)
    dir = DIRS[(index + (amount//90)) % 4]
    return pos, dir
def north(pos, dir, amount):
    pos = (pos[0], pos[1] - amount)
    return pos, dir
def south(pos, dir, amount):
    pos = (pos[0], pos[1] + amount)
    return pos, dir
def west(pos, dir, amount):
    pos = (pos[0] - amount, pos[1])
    return pos, dir
def east(pos, dir, amount):
    pos = (pos[0] + amount, pos[1])
    return pos, dir

INSTRUCTIONS = {
    'F': forward,
    'L': left,
    'R': right,
    'N': north,
    'S': south,
    'E': east,
    'W': west,
}

with open(sys.argv[1]) as file:
    for line in file:
        instruction = line[0]
        amount = int(line[1:])
        print(pos, dir)
        pos, dir = INSTRUCTIONS[instruction](pos, dir, amount)

print(abs(pos[0] + abs(pos[1])))
