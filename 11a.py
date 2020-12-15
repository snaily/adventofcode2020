import sys

old_plan = []
with open(sys.argv[1]) as file:
    for line in file:
        old_plan.append(line.strip())

def generation(plan):
    next_plan = []
    for y, line in enumerate(plan):
        next_plan.append(['0'] * len(line))
        for x, _ in enumerate(line):
            neighbors = 0
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if not (0 <= x+dx < len(line)) or not (0 <= y+dy < len(plan)):
                        continue
                    if plan[y+dy][x+dx] == '#':
                        neighbors += 1
            if plan[y][x] == 'L' and neighbors == 0:
                next_plan[y][x] = '#'
            elif plan[y][x] == '#' and neighbors >= 5: # not 4, because we count ourselves above
                next_plan[y][x] = 'L'
            else:
                next_plan[y][x] = plan[y][x]
    return next_plan

new_plan = generation(old_plan)
while new_plan != old_plan:
    print(str('\n'.join(''.join(line) for line in new_plan)),'\n')
    old_plan, new_plan = new_plan, generation(new_plan)

print(sum(line.count('#') for line in new_plan))
