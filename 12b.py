import sys

pos = (0, 0)
wp = (10, -1)

def forward(pos, wp, amount):
    pos = (pos[0] + amount*wp[0], pos[1] + amount*wp[1])
    return pos, wp
def left(pos, wp, amount):
    for _ in range(amount//90):
        wp = (wp[1], -wp[0])
    return pos, wp
def right(pos, wp, amount):
    for _ in range(amount//90):
        wp = (-wp[1], wp[0])
    return pos, wp
def north(pos, wp, amount):
    wp = (wp[0], wp[1] - amount)
    return pos, wp
def south(pos, wp, amount):
    wp = (wp[0], wp[1] + amount)
    return pos, wp
def west(pos, wp, amount):
    wp = (wp[0] - amount, wp[1])
    return pos, wp
def east(pos, wp, amount):
    wp = (wp[0] + amount, wp[1])
    return pos, wp

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
        pos, wp = INSTRUCTIONS[instruction](pos, wp, amount)
        print(pos, wp)

print(abs(pos[0]) + abs(pos[1]))
