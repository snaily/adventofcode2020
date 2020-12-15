import sys

joltages = [0]
with open(sys.argv[1]) as file:
    for line in file:
        joltages.append(int(line))
joltages.append(max(joltages) + 3)

joltages.sort(reverse=True)
counts = [0] * len(joltages)
counts[0] = 1
print(joltages)
# how many ways can we get from jolts to target joltage?
for i in range(len(joltages)):
    for j in range(1, 4):
        if i - j >= 0 and joltages[i-j] - joltages[i] <= 3:
            counts[i] += counts[i-j]

print(counts[-1])