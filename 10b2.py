import sys
import functools

joltages = [0]
with open(sys.argv[1]) as file:
    for line in file:
        joltages.append(int(line))
joltages.append(max(joltages) + 3)

joltages.sort()
# memoized naive recursion
@functools.lru_cache(maxsize=None)
def combinations(i):
    if i == len(joltages) - 1:
        return 1
    n = 0
    for j in range(1, 4):
        if i+j < len(joltages):
            if joltages[i+j] <= joltages[i] + 3:
                n += combinations(i+j)
    return n
print(combinations(0))
print(combinations.cache_info())