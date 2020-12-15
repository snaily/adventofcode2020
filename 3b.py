import sys

speeds = ((1,1), (3,1), (5,1), (7,1), (1,2))
trees = [0] * len(speeds)
x = [0] * len(speeds)
with open(sys.argv[1]) as file:
    for y, line in enumerate(file):
        line = line.strip()
        for i, (dx, dy) in enumerate(speeds):
            if y % dy != 0:
                continue    
            if line[x[i]] == '#':
                trees[i] += 1
            x[i] = (x[i] + dx) % len(line)

product = 1
for tree in trees:
    product *= tree
print(product)
