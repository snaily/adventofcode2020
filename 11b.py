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
                    if dy == 0 and dx == 0:
                        continue
                    for i in range(1,len(line)):
                        if not (0 <= x+i*dx < len(line)) or not (0 <= y+i*dy < len(plan)):
                            break
                        if plan[y+i*dy][x+i*dx] == 'L':
                            break
                        if plan[y+i*dy][x+i*dx] == '#':
                            neighbors += 1
                            break
            if plan[y][x] == 'L' and neighbors == 0:
                next_plan[y][x] = '#'
            elif plan[y][x] == '#' and neighbors >= 5:
                next_plan[y][x] = 'L'
            else:
                next_plan[y][x] = plan[y][x]
    return next_plan

new_plan = generation(old_plan)
while new_plan != old_plan:
    #print(str('\n'.join(''.join(line) for line in new_plan)),'\n')
    old_plan, new_plan = new_plan, generation(new_plan)

print(sum(line.count('#') for line in new_plan))
