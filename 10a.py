import sys

joltages = [0]
with open(sys.argv[1]) as file:
    for line in file:
        joltages.append(int(line))
joltages.append(max(joltages) + 3)

joltages.sort()
differences = list(map(lambda a, b: b-a, joltages[:-1], joltages[1:]))
print(differences.count(1) * differences.count(3))
