import sys

group = set()
total = 0
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        if line == '':
            total += len(group)
            group.clear()
            continue
        group.update(line)
print(total)