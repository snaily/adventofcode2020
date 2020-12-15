import sys

trees = 0
pos = 0
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        if line[pos] == '#':
            trees += 1
        pos = (pos + 3) % len(line)
print(trees)
